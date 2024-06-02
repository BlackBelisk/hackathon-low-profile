import subprocess
import time

def start_scrcpy():
    try:
        # Command to execute scrcpy in a separate process
        subprocess.Popen(["scrcpy-win64-v2.4/scrcpy.exe"])
    except subprocess.CalledProcessError as e:
        print(f"Error executing scrcpy: {e}")

def launch_app(package_name):
    try:
        # Command to launch the specific app using ADB with full path specified
        adb_path = r"scrcpy-win64-v2.4/adb.exe" 
        subprocess.run([adb_path, "shell", "monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching the app: {e}")

def get_device_model():
    try:
        # Run adb shell getprop command to retrieve device properties
        adb_path = r"scrcpy-win64-v2.4/adb.exe"
        result = subprocess.run([adb_path, "shell", "getprop", "ro.product.model"], capture_output=True, text=True, check=True)
        device_model = result.stdout.strip()
        return device_model
    except subprocess.CalledProcessError as e:
        print(f"Error getting device model: {e}")
        return None

def doxxeo():
    start_scrcpy()
    
    # Package name of the app you want to open
    #app_package_name = "com.google.android.apps.authenticator2"
    app_package_name = "com.example.Gen"
    
    # Wait for a few seconds to allow scrcpy to start
    time.sleep(2)
    
    # Launch the specific app
    launch_app(app_package_name)


