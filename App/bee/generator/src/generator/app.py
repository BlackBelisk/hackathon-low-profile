import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import random
import os

# Función para generar un token de 6 dígitos
def generate_token():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

# Función para generar un archivo de texto con el token
def generate_text_file(token):
    text_content = f"Token generado: {token}"
    with open("generated_token.txt", "w") as file:
        file.write(text_content)

class NumGenerator(toga.App):
    def startup(self):
        # Crear la ventana principal
        self.main_window = toga.MainWindow(title=self.formal_name)
        
        # Crear un Box para los widgets
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        
        # Crear un Label para mostrar el token
        self.token_label = toga.Label('Generando token...', style=Pack(padding=10))
        main_box.add(self.token_label)

        # Programar la actualización del token
        self.update_token(None)  # Actualizar inmediatamente
        self.timer = self.main_window.set_timer(15, self.update_token)  # Actualizar cada 15 segundos

        # Configurar la ventana principal
        self.main_window.content = main_box
        self.main_window.show()

    def update_token(self, widget):
        # Generar el token y actualizar el Label
        token = generate_token()
        self.token_label.text = token
        generate_text_file(token)

def main():
    return NumGenerator()

if __name__ == '__main__':
    main().main_loop()
