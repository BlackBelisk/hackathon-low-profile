import subprocess
import time

def start_scrcpy():
    try:
        #scrcpy_path = r"C:\Users\Usuario\Downloads\scrcpy\scrcpy.exe"  # Add the full path to the scrcpy executable
        # Command to execute scrcpy
        subprocess.run(["scrcpy"], check=True)  # Use the full path
    except subprocess.CalledProcessError as e:
        print(f"Error executing scrcpy: {e}")

def launch_app(package_name):
    try:
        # Command to launch the specific app using ADB
        cmd_com = "adb shell monkey -p com.google.android.apps.authenticator2 -c android.intent.category.LAUNCHER 1"
        subprocess.run(["adb", "shell", cmd_com])#"monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error launching the app: {e}")

def main():
    # Start scrcpy
    start_scrcpy()
    
    # Package name of the app you want to open
    app_package_name = "com.whatsapp"  # Replace with the actual package name of the app
    time.sleep(2)
    # Launch the specific app
    launch_app(app_package_name)

if __name__ == "__main__":
    main()
