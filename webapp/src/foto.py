from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.adb_message import AdbMessage
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
import subprocess
import time
#from src import screen
#from src import conectandoDispositivo
from src import intento
# Función para tomar una foto usando ADB
def take_photo(cam, id):
    # Comando ADB para tomar una foto
    adb_cmd3 = "input keyevent KEYCODE_CAMERA"
    intento.launch_app(cam, id)
    time.sleep(3)
    subprocess.run(["adb", "-s", id,"shell", adb_cmd3])
    time.sleep(2)


# Función para obtener la foto desde el dispositivo
def get_photo(id):
    # Comando ADB para copiar la foto al almacenamiento externo del dispositivo
    adb_cmd = "/storage/emulated/0/DCIM/Camera/*.jpg"
    # Ejecutar el comando ADB
    result = subprocess.run(["adb", "-s", id, "shell", "ls", "-t", "-1", adb_cmd], capture_output=True, text=True)
    photo = result.stdout.splitlines()[0].strip()
    filename = "webapp/photo.png"
    # Comando ADB para copiar el archivo al directorio actual
    adb_cmd = ""
    # Ejecutar el comando ADB
    subprocess.run(["adb", "-s", id, "pull", photo, filename])


