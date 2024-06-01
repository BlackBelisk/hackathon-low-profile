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


def main():
    start_scrcpy()
    
    # Package name of the app you want to open
    app_package_name = "com.google.android.apps.authenticator2"
    
    # Wait for a few seconds to allow scrcpy to start
    time.sleep(2)
    
    # Launch the specific app
    launch_app(app_package_name)

if __name__ == "__main__":
    main()
