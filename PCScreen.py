import pyautogui
import time
from PIL import Image


time.sleep(2)
pyautogui.mouseInfo()
# Capturar la pantalla completa y guardarla como "screenshot.png"
pyautogui.screenshot("screenshot.png")

# Abrir la imagen con Pillow
imagen = Image.open("screenshot.png")

# Definir las coordenadas y dimensiones del recorte (x, y, ancho, alto)
x = 972
y = 129
ancho = 611
alto = 1129

# Recortar la imagen
recorte = imagen.crop((x, y, x + ancho, y + alto))

# Guardar el recorte como "recorte.png"
recorte.save("recorte.png")
