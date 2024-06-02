import ScreenVentana
import intento
import time
if __name__ == "__main__":
    if (intento.doxxeo()):
        time.sleep(3) 
        window_title = ScreenVentana.get_device_model() # Especifica el título de la ventana que deseas capturar
        output_file = "screenshot.png" # Especifica el nombre del archivo de salida
        ScreenVentana.bring_window_to_front(window_title)  # Traer la ventana al frente
        ScreenVentana.capture_window(window_title, output_file) # Capturar la ventana