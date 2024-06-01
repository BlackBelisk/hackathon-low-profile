import ScreenVentana
import intento
import time
if __name__ == "__main__":
    intento.doxxeo()

    time.sleep(3)

    # Especifica el título de la ventana que deseas capturar
    window_title = ScreenVentana.get_device_model()
    
    # Especifica el nombre del archivo de salida
    output_file = "screenshot.png"
    
    # Traer la ventana al frente
    ScreenVentana.bring_window_to_front(window_title)
    
    # Capturar la ventana
    ScreenVentana.capture_window(window_title, output_file)