import usb.core
import usb.util
import time
import usb.backend.libusb1

# Intentar obtener el backend de libusb
backend = usb.backend.libusb1.get_backend()

if backend is None:
    print("No se encontró el backend de libusb. Asegúrate de que libusb-1.0.dll está en el PATH.")
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
