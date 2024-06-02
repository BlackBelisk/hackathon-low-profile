import usb.core
import usb.util
import usb.backend.libusb1
import subprocess
import time

# Obtener el backend de libusb
backend = usb.backend.libusb1.get_backend()

if backend is None:
    print("No se encontró el backend de libusb. Asegúrate de que libusb-1.0.dll está en el PATH.")
else:
    print("Backend de libusb encontrado correctamente.")

def find_usb_devices():
    # Buscar todos los dispositivos USB
    return usb.core.find(find_all=True, backend=backend)

def restart_adb_server():
    subprocess.run(['adb', 'kill-server'])
    subprocess.run(['adb', 'start-server'])

def get_connected_devices():
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')[1:]
    devices = [line.split('\t')[0] for line in lines if 'device' in line]
    return devices

def take_screenshot():
    # Tomar una captura de pantalla y guardarla en el almacenamiento interno
    subprocess.run(['adb', 'shell', 'screencap', '-p', '/storage/emulated/0/screenshot.png'])
    print("Captura de pantalla tomada y guardada en /storage/emulated/0/screenshot.png")

def main():
    restart_adb_server()
    while True:
        usb_devices = list(find_usb_devices())
        if usb_devices:
            print("Dispositivo USB detectado")
            adb_devices = get_connected_devices()
            if adb_devices:
                print(f"Dispositivo Android conectado a ADB: {adb_devices[0]}")
                take_screenshot()
                break
            else:
                print("Esperando conexión ADB del dispositivo Android...")
                time.sleep(1)
        else:
            print("Esperando conexión de dispositivo USB...")
            time.sleep(1)

if __name__ == "__main__":
    main()
