import subprocess

def take_screenshot():
    # Comando para tomar una captura de pantalla
    command = ["adb", "shell", "screencap", "/sdcard/token.png"]
    subprocess.run(command)
    
    command = ["adb", "pull", "/sdcard/token.png", "."]
    subprocess.run(command)

    print("Captura de pantalla tomada y guardada como 'screenshot.png'")