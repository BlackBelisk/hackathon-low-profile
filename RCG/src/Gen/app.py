import random
import asyncio
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
        self.add_background_task(self.update_code)

    async def update_code(self, widget, **kwargs):
        while(True):
        # Generar un código de 6 dígitos aleatorios
            random_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            self.label.text = random_code
        # Esperar 5 segundos antes de la próxima actualización
            await asyncio.sleep(5)

   
def main():
    app = RandomCodeApp('Random Code Generator', 'org.example.randomcode')
    ##update_code(app)
    return app
    ##app.add_background_task()

if __name__ == '__main__':
    main().main_loop()
