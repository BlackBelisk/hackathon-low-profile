import kivy
kivy.require('2.3.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import random

#App to generate a token composed of 6 digits that updates every 15 seconds

def generate_token():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

def generate_text_file(token):
    text_content = f"Token generado: {token}"
    with open("generated_token.txt", "w") as file:
        file.write(text_content)

class Root(BoxLayout):
    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.orientation = 'vertical'
        Clock.schedule_once(self.update_token, 0)  # Update immediately
        Clock.schedule_interval(self.update_token, 15)  # Update every 15 seconds

    def update_token(self, dt):
        token = generate_token()
        self.random_label.text = token
        generate_text_file(token)

class NumGenerator(App):
    def build(self):
        return Root()

if __name__ == '__main__':
    numGen = NumGenerator()
    numGen.run()
