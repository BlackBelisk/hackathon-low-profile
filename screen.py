import subprocess

def take_screenshot():
    # Comando para tomar una captura de pantalla
    command = ["adb", "shell", "screencap", "/sdcard/screenshot.png"]
    subprocess.run(command)
    
    print("Captura de pantalla tomada y guardada como 'screenshot.png'")

# Llama a la función para tomar la captura de pantalla
take_screenshot()
