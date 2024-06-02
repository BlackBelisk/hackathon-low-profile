import subprocess
import time

adb_path = r"scrcpy-win64-v2.4/adb.exe"

def scroll_down(duration_ms=500):
    # La posición de inicio y fin del scroll (ajusta según sea necesario)
    start_x = 500
    start_y = 1500
    end_x = 500
    end_y = 500

    # Convertir la duración de milisegundos a segundos
    duration_s = duration_ms / 1000
    
    
    # Comando adb para enviar el evento de desplazamiento
    command = [
        adb_path, "shell",
        "input",
        "swipe",
        str(start_x),
        str(start_y),
        str(end_x),
        str(end_y),
        str(duration_ms)
    ]

    # Ejecutar el comando
    subprocess.run(command)

def main():
    # Asegurarse de que el dispositivo está conectado
    try:
        subprocess.run([adb_path, "start-server"], check=True)
    except subprocess.CalledProcessError:
        print("Error al iniciar el servidor ADB.")
        return

    # Iniciar scrcpy en un proceso separado
    try:
        scrcpy_process = subprocess.Popen(["scrcpy-win64-v2.4/scrcpy.exe"])
        time.sleep(2)  # Esperar a que scrcpy se inicie completamente

        # Desplazar hacia abajo varias veces
        for _ in range(5):  # Ajusta el número de desplazamientos según sea necesario
            scroll_down()
            time.sleep(1)  # Esperar un segundo entre desplazamientos

        # Terminar scrcpy
        scrcpy_process.terminate()
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
