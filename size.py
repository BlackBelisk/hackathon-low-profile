import subprocess

# Función para obtener la resolución del dispositivo
def get_device_resolution():
    # Ejecutar el comando adb para obtener el tamaño de la pantalla
    result = subprocess.run(["adb", "shell", "wm", "size"], capture_output=True, text=True)
    
    # Extraer la resolución de la salida del comando
    output = result.stdout
    if "Physical size:" in output:
        resolution = output.split("Physical size: ")[1].strip()
        return resolution
    else:
        raise RuntimeError("No se pudo obtener la resolución del dispositivo")

# Llamar a la función y mostrar la resolución
try:
    resolution = get_device_resolution()
    print(f"La resolución del dispositivo es: {resolution}")
except Exception as e:
    print(f"Error: {e}")
