import random
import time
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from toga import App, Box, Label, MainWindow

class RandomCodeApp(App):
    def startup(self):
        self.main_window = MainWindow(title=self.formal_name)
        
        self.main_box = Box(style=Pack(direction=COLUMN, alignment=CENTER))

        self.label = Label("000000", style=Pack(padding=20, font_size=48, text_align=CENTER))
        self.main_box.add(self.label)

        self.main_window.content = self.main_box
        self.main_window.show()

        self.update_code()

    def update_code(self):
        while True:
            # Generar un código de 6 dígitos aleatorios
            random_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            self.label.text = random_code
            # Esperar 5 segundos antes de la próxima actualización
            time.sleep(5.0)

def main():
    return RandomCodeApp('Random Code Generator', 'org.example.randomcode')

if __name__ == '__main__':
    main().main_loop()
