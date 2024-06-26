import usb.core
import usb.util
import usb.backend.libusb1
import subprocess
from src import identifier

# Obtener el backend de libusb
backend = usb.backend.libusb1.get_backend()
ids = {'0x2717', '0x04e8', '0x12D1', '0x22b8', '0x0421', '0x18d1', '0x22D9'}
if backend is None:
    print("No se encontró el backend de libusb. Asegúrate de que libusb-1.0.dll está en el PATH.")
else:
    print("Backend de libusb encontrado correctamente.")

def find_android_device():
    device = identifier.get_last_connected_device()
    if device:
        elem = list(device)
    if device and elem[0] in ids:
        return usb.core.find(find_all=True, idVendor=device, backend=backend)  # idVendor es el ID de Google para dispositivos Android
    else:
        return None

def restart_adb_server():
    subprocess.run(['adb', 'kill-server'])
    subprocess.run(['adb', 'start-server'])

def get_connected_devices():
    adb_path = r"scrcpy-win64-v2.4/adb.exe"
    result = subprocess.run([adb_path, 'devices'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')[1:]  # Ignorar la primera línea
    devices = [line.split('\t')[0] for line in lines if 'device' in line]
    print(devices)
    return devices

def captura():
    ##restart_adb_server()
    #while True:
    device = find_android_device()
    if device:
        print("Dispositivo Android detectado por USB")
        adb_devices = get_connected_devices()
        if adb_devices:
            print(f"Dispositivo Android conectado a ADB: {adb_devices[0]}")
            #time.sleep(1)
            return True
        else:
            print("Esperando conexión ADB del dispositivo Android...")
            #time.sleep(1)
            return False
    else:
        print("Esperando conexión de dispositivo Android por USB...")
        #time.sleep(1)
        return False