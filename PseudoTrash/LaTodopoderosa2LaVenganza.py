import intento
import time
import foto
import conectandoDispositivo

def hackear():
    devices = conectandoDispositivo.get_connected_devices()
    ventana = intento.doxxeo(devices[1])
    time.sleep(50)
    if (ventana):
        time.sleep(3)
        foto.take_photo()
        #window_title = intento.get_device_model() # Especifica el título de la ventana que deseas capturar
        #output_file = "screen.png" # Especifica el nombre del archivo de salida
        #ScreenVentana.bring_window_to_front(window_title)  # Traer la ventana al frente
        #ScreenVentana.capture_window(window_title, output_file) # Capturar la ventana
        intento.end_srcrpy(ventana)
        
hackear()