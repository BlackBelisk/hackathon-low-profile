import usb.core
import usb.util
import usb.backend.libusb1
import time
import win32file
import win32event
import win32con
import screen
import identifier

def list_usb_devices():
    devices = [dev for dev in usb.core.find(find_all=True)]
    return devices

def detect_usb_events():
    # Create an event to wait for device notifications
    hDeviceNotify = win32file.FindFirstChangeNotification(
        "C:\\",  # This should be the drive where your USB devices appear
        True,
        win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES | win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
        win32con.FILE_NOTIFY_CHANGE_FILE_NAME | win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
        win32con.FILE_NOTIFY_CHANGE_SECURITY | win32con.FILE_NOTIFY_CHANGE_SIZE
    )
    
    if hDeviceNotify == win32file.INVALID_HANDLE_VALUE:
        raise RuntimeError("Failed to create notification handle")

    try:
        initial_devices = list_usb_devices()
        while True:
            # Wait for an event to occur
            result = win32event.WaitForSingleObject(hDeviceNotify, 500)

            if result == win32event.WAIT_OBJECT_0:
                current_devices = list_usb_devices()
                if len(current_devices) > len(initial_devices):
                    device = identifier.get_last_connected_device()
                    if device:
                        print(device)
                elif len(current_devices) < len(initial_devices):
                    identifier.get_last_connected_device()  # Device disconnected
                    print("Dispositivo desconectado.")
                
                initial_devices = current_devices

                # Reset the notification handle
                win32file.FindNextChangeNotification(hDeviceNotify)
    finally:
        win32file.FindCloseChangeNotification(hDeviceNotify)

if __name__ == "__main__":
    detect_usb_events()
