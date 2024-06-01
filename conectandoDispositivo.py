import usb.core
import usb.util
import usb.backend.libusb1
import time
from adb_shell.adb_device import AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
import os
import subprocess

# Obtener el backend de libusb
backend = usb.backend.libusb1.get_backend()

if backend is None:
    print("No se encontró el backend de libusb. Asegúrate de que libusb-1.0.dll está en el PATH.")
else:
    print("Backend de libusb encontrado correctamente.")

    def find_android_device():
        # Filtrar dispositivos USB para encontrar el dispositivo Android
        return usb.core.find(find_all=True, idVendor=0x18d1, backend=backend)  # idVendor es el ID de Google para dispositivos Android

    def take_screenshot():
    # Comando para tomar una captura de pantalla
        command = ["adb", "shell", "screencap", "/sdcard/screenshot.png"]
        subprocess.run(command)
    
    print("Captura de pantalla tomada y guardada como 'screenshot.png'")

    def main():
        while True:
            devices = list(find_android_device())
            if devices:
                print("Dispositivo Android conectado")
                take_screenshot()
                break
            else:
                print("Esperando conexión de dispositivo Android...")
                time.sleep(1)

    if __name__ == "__main__":
        main()
