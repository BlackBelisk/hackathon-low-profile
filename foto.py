from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.adb_message import AdbMessage
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
import subprocess
import time
import intento
import screen

# Función para tomar una foto usando ADB
def take_photo():
    # Comando ADB para tomar una foto (puede variar dependiendo del dispositivo)
    #adb_cmd = "input keyevent KEYCODE_CAMERA"
    adb_cmd1 = "am start -a android.media.action.IMAGE_CAPTURE"
    adb_cmd2 = "input keyevent KEYCODE_FOCUS"
    adb_cmd3 = "input keyevent KEYCODE_CAMERA"
    adb_cmd4 = "input tap 645 1918"
    adb_cmd5 = "input tap 853 1470"
    
    # Ejecutar el comando ADB
    subprocess.run(["adb", "shell", adb_cmd1])
    #intento.launch_app("com.android.camera")
    time.sleep(2)
    subprocess.run(["adb", "shell", adb_cmd2])
    time.sleep(2)
    screen.take_screenshot()
    #subprocess.run(["adb", "shell", adb_cmd3])
    #time.sleep(2)
    #subprocess.run(["adb", "shell", adb_cmd4])


# Función para obtener la foto desde el dispositivo
def get_photo():
    # Comando ADB para copiar la foto al almacenamiento externo del dispositivo
    adb_cmd = "cp /sdcard/DCIM/Camera/* /sdcard/"
    # Ejecutar el comando ADB
    subprocess.run(["adb", "shell", adb_cmd])
    # Comando ADB para listar los archivos en el almacenamiento externo
    adb_cmd = "ls /sdcard/*.jpg"
    # Ejecutar el comando ADB y obtener la lista de archivos
    result = subprocess.run(["adb", "shell", adb_cmd], capture_output=True, text=True)
    # Obtener el nombre del archivo de la lista
    filename = result.stdout.strip()
    # Comando ADB para copiar el archivo al directorio actual
    adb_cmd = f"pull {filename} ."
    # Ejecutar el comando ADB
    subprocess.run(["adb", adb_cmd])

# Tomar una foto
take_photo()
# Obtener la foto
#get_photo()
