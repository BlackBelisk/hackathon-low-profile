import tkinter as tk
import random
import time
import conectandoDispositivo

class TokenSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Token Simulator")

        self.token_label = tk.Label(root, text="Press the button to generate token", font=("Helvetica", 18))
        self.token_label.pack(pady=20)

        self.generate_button = tk.Button(root, text="Generate Token", command=self.hacerCaptura, font=("Helvetica", 18))
        self.generate_button.pack(pady=20)

    def hacerCaptura(self):
        conectandoDispositivo.tomarCaptura()

if __name__ == "__main__":
    root = tk.Tk()
    app = TokenSimulator(root)
    root.mainloop()
