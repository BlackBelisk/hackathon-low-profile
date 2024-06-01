import random
import threading
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
        # Generar un código de 6 dígitos aleatorios
        random_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        self.label.text = random_code
        # Llamar a esta función de nuevo en 5 segundos
        threading.Timer(5.0, self.update_code).start()

def main():
    return RandomCodeApp('Random Code Generator', 'org.example.randomcode')

if __name__ == '__main__':
    main().main_loop()