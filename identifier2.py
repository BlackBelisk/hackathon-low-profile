import usb.core
import usb.util
import win32file
import win32con
import win32api

# Almacenar el estado de los dispositivos USB conectados
previous_devices = []

def get_device_info(device):
    try:
        return {
            "idVendor": hex(device.idVendor),
            "idProduct": hex(device.idProduct),
        }
    except usb.core.USBError as e:
        print(f"Error al obtener información del dispositivo: {e}")
        return None

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
    
    # Actualizar la lista de dispositivos anteriores
    previous_devices = current_devices

    # Devolver la información del nuevo dispositivo
    if new_device:
        return get_device_info(new_device)
    else:
        return None

# Inicializar la lista de dispositivos USB actuales
update_device_list()

# Llama a esta función cuando desees obtener información del último dispositivo conectado
def main():
    last_device_info = get_last_connected_device()
    if last_device_info:
        print("Nuevo dispositivo conectado:")
        print(last_device_info)
    else:
        print("No se ha conectado ningún dispositivo nuevo.")

if __name__ == "__main__":
    main()
