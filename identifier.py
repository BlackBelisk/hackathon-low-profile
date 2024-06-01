import usb.core
import usb.util
import win32file
import win32con
import win32api

previous_devices = [dev for dev in usb.core.find(find_all=True)]

def update_device_list():
    global previous_devices
    previous_devices = list(usb.core.find(find_all=True))

def get_last_connected_device():
    global previous_devices
    current_devices = list(usb.core.find(find_all=True))
    
    # Identificar el nuevo dispositivo
    new_device = None
    for device in current_devices:
        if device not in previous_devices:
            new_device = device
            break
    
    # Identificar el dispositivo desconectado
    disconnected_device = None
    for device in previous_devices:
        if device not in current_devices:
            disconnected_device = device
            break
        
    # Actualizar la lista de dispositivos anteriores
    previous_devices = current_devices

    # Devolver la información del nuevo dispositivo
    if new_device:
        return find_device(new_device)
    else:
        return None

update_device_list()

def find_device(device):
    try:
        return {
            "idVendor": hex(device.idVendor),
            "idProduct": hex(device.idProduct),
        }
    except usb.core.USBError as e:
        print(f"Error al obtener información del dispositivo: {e}")
        return None
