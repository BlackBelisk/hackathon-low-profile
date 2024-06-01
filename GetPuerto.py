import usb.core
import usb.util
import usb.backend.libusb1
import time
import win32file
import win32event
import win32con

def list_usb_devices():
    devices = [dev for dev in usb.core.find(find_all=True)]
    return devices

def get_usb_device_port(device):
    return device.bus, device.address

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
                for device in current_devices:
                    if device not in initial_devices:
                        print(f"New device connected to port: {get_usb_device_port(device)}")
                        break
                
                for device in initial_devices:
                    if device not in current_devices:
                        print(f"Device disconnected from port: {get_usb_device_port(device)}")
                        break
                
                initial_devices = current_devices

                # Reset the notification handle
                win32file.FindNextChangeNotification(hDeviceNotify)
    finally:
        win32file.FindCloseChangeNotification(hDeviceNotify)

if __name__ == "__main__":
    detect_usb_events()
