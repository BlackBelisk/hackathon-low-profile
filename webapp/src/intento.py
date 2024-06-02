import subprocess
import time
from src import conectandoDispositivo


def start_scrcpy(id):
    try:
        # Command to execute scrcpy in a separate process
        path = "scrcpy-win64-v2.4/scrcpy.exe"
        ventana = subprocess.Popen([path, "-s", id])
        return ventana
    except subprocess.CalledProcessError as e:
        print(f"Error executing scrcpy: {e}")

def end_srcrpy(ventana):
    ventana.terminate()
    ventana.wait()

def launch_app(package_name, id):
    try:
        # Command to launch the specific app using ADB with full path specified
        adb_path = r"scrcpy-win64-v2.4/adb.exe" 
        subprocess.run([adb_path,"-s", id, "shell", "monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching the app: {e}")

def close_app(package_name, id):
    try:
        # Command to launch the specific app using ADB with full path specified
        adb_path = r"scrcpy-win64-v2.4/adb.exe" 
        adb_cmd = "am force-stop"
        subprocess.run([adb_path,"-s", id, "shell", adb_cmd, package_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching the app: {e}")

def get_device_model(id):
    try:
        # Run adb shell getprop command to retrieve device properties
        adb_path = r"scrcpy-win64-v2.4/adb.exe"
        result = subprocess.run([adb_path, "-s", id, "shell", "getprop", "ro.product.model"], capture_output=True, text=True, check=True)
        device_model = result.stdout.strip()
        return device_model
    except subprocess.CalledProcessError as e:
        print(f"Error getting device model: {e}")
        return None

def get_android_version(id):
    try:
        # Ejecutar el comando adb shell getprop ro.build.version.release y capturar la salida
        adb_path = r"scrcpy-win64-v2.4/adb.exe"
        result = subprocess.run([adb_path, "-s", id, "shell", "getprop", "ro.build.version.release"], capture_output=True, text=True, check=True)
        
        # Extraer y devolver la versión de Android del resultado
        android_version = result.stdout.strip()
        return android_version
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener la versión de Android: {e}")
        return None
    
def doxxeo(id):
    ventana = start_scrcpy(id)
    version_android = get_android_version(id)

    if version_android:
        print(f"Versión de Android del dispositivo: {version_android}")
        try:
            android_version_int = int(version_android)
            if android_version_int >= 11:
                print("No es posible duplicar la pantalla de Google Authenticator.")
                app_package_name = "com.example.Gen"
            else:
                app_package_name = "com.google.android.apps.authenticator2" # Package name of the app you want to open
            launch_app(app_package_name, id)
            time.sleep(2)
            return ventana
        except ValueError:
            print("La versión de Android no es un número válido.")
    else:
        print("No se pudo obtener la versión de Android del dispositivo.")
    return False
