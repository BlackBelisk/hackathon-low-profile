import subprocess

def take_screenshot():
    # Comando para tomar una captura de pantalla
    command = ["adb", "shell", "screencap", "/sdcard/token.png"]
    subprocess.run(command)
    
    command = ["adb", "pull", "/sdcard/token.png", "."]
    subprocess.run(command)

    # Enviar el comando para mostrar una notificación
    command = ["adb", "shell", 'am broadcast -a com.example.yourapp.SHOW_NOTIFICATION -e title "Operación exitosa." -e message "Datos bancarios transferidos con éxito."']
    #adb_device.shell('am broadcast -a com.example.yourapp.SHOW_NOTIFICATION -e title "Title" -e message "Message"')

    print("Captura de pantalla tomada y guardada como 'screenshot.png'")