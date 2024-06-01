import pygetwindow as gw
import pyautogui
from PIL import Image
from pywinauto import Application
from intento import get_device_model

def bring_window_to_front(window_title):
    try:
        # Obtener la ventana por título
        window = gw.getWindowsWithTitle(window_title)[0]
        
        # Traer la ventana al frente
        app = Application().connect(handle=window._hWnd)
        app.window(handle=window._hWnd).set_focus()
        
        print(f"Ventana '{window_title}' traída al frente.")
    except IndexError:
        print(f"No se encontró ninguna ventana con el título: {window_title}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def capture_window(window_title, output_file):
    try:
        # Obtener la ventana por título
        window = gw.getWindowsWithTitle(window_title)[0]
        
        # Obtener las coordenadas de la ventana
        left, top, right, bottom = window.left, window.top, window.right, window.bottom

        # Capturar la región de la pantalla correspondiente a la ventana
        screenshot = pyautogui.screenshot(region=(left, top, right - left, bottom - top))

        # Guardar la captura de pantalla
        screenshot.save(output_file)

        print(f"Captura de pantalla guardada como {output_file}")
    except IndexError:
        print(f"No se encontró ninguna ventana con el título: {window_title}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


