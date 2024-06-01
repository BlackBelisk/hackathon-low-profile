import os
import time
import usb.core
import usb.util
import usb.backend.libusb1

# Especificar manualmente la ruta de libusb-1.0.dll
dll_path = os.path.abspath('libusb-1.0.dll')

if not os.path.exists(dll_path):
    print(f"libusb-1.0.dll no se encuentra en {dll_path}.")
else:
    backend = usb.backend.libusb1.get_backend(find_library=lambda x: dll_path)

    if backend is None:
        print("No se encontró el backend de libusb. Asegúrate de que libusb-1.0.dll está en la carpeta del proyecto.")
    else:
        print("Backend de libusb encontrado correctamente.")
        
        def find_usb_device():
            return usb.core.find(find_all=True, backend=backend)

        def main():
            connected_devices = set()

            while True:
                current_devices = set(find_usb_device())

                # Check for new devices
                new_devices = current_devices - connected_devices
                if new_devices:
                    print("1")
                    connected_devices = current_devices

                # Check for removed devices
                removed_devices = connected_devices - current_devices
                if removed_devices:
                    print("0")
                    connected_devices = current_devices

                time.sleep(1)

        if __name__ == "__main__":
            main()
