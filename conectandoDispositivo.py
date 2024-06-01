import usb.core
import usb.util
import usb.backend.libusb1
import time
from adb_shell.adb_device import AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
import os

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
        adbkey = '"C:\Users\Admin\.android"'

        # Cargar la clave privada para la autenticación
        with open(adbkey) as f:
            priv = f.read()
        with open(f'{adbkey}.pub') as f:
            pub = f.read()

        signer = PythonRSASigner(pub, priv)

        # Conectar al dispositivo (asegúrate de que la depuración USB esté habilitada en el dispositivo)
        device = AdbDeviceUsb()

        # Autenticar
        device.connect(rsa_keys=[signer], auth_timeout_s=0.1)

        # Tomar una captura de pantalla y guardarla en el almacenamiento interno
        device.shell('screencap -p /storage/emulated/0/screenshot.png')
        print("Captura de pantalla tomada y guardada en /storage/emulated/0/screenshot.png")

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
