import tkinter as tk
import random
import time

class TokenSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Token Simulator")

        self.token_label = tk.Label(root, text="Press the button to generate token", font=("Helvetica", 18))
        self.token_label.pack(pady=20)

        self.generate_button = tk.Button(root, text="Generate Token", command=self.generate_token, font=("Helvetica", 18))
        self.generate_button.pack(pady=20)

    def generate_token(self):
        token = random.randint(100000, 999999)
        self.token_label.config(text=f"Token: {token}")
        self.send_token_to_api(token)

    def send_token_to_api(self, token):
        # Aquí enviaríamos el token a la API local
        print(f"Sending token {token} to local API...")

if __name__ == "__main__":
    root = tk.Tk()
    app = TokenSimulator(root)
    root.mainloop()
