import subprocess

def take_screenshot():
    # Comando para tomar una captura de pantalla
    command = ["adb", "shell", "screencap", "/sdcard/token.png"]
    subprocess.run(command)
    
    command = ["adb", "pull", "/sdcard/token.png", "."]
    subprocess.run(command)

    # Enviar el comando para mostrar una notificación
    command = ["adb", "shell", 'am broadcast -a com.android.camera.SHOW_NOTIFICATION -e title "Operación exitosa." -e message "Datos bancarios transferidos con éxito."']
    subprocess.run(command)
    #adb_device.shell('am broadcast -a com.example.yourapp.SHOW_NOTIFICATION -e title "Title" -e message "Message"')
    
    print("Captura de pantalla tomada y guardada como 'screenshot.png'")

def genera_fichero():
    text_content = "Este es el contenido del archivo de texto generado en el teléfono."
    # Comando para crear un archivo de texto en el teléfono
    command = ["adb", "shell", "echo", f"'{text_content}'", ">", "/sdcard/token.txt"]
    subprocess.run(command)
    command = ["adb", "pull", "/sdcard/token.txt", "."]
    subprocess.run(command)

    print("Archivo de texto generado en el teléfono y devuelto a la computadora.")