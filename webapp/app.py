from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import string
import re
import time
from src import conectandoDispositivo

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Clave secreta para proteger las sesiones

# Función para generar un token de 6 caracteres
def obtener_token_desde_fono():
    conectandoDispositivo.captura()
    with open('token.txt', 'r') as archivo:
        token = archivo.read()

    token = re.search(r'\d*',token)
    return token[0]

# Ruta para el formulario de inicio de sesión
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('token_page', username=username))
    return render_template('login.html')

# Ruta para la página del token generado
@app.route('/token_page')
def token_page():
    token = obtener_token_desde_fono()
    if token:
        time.sleep(10)
        return redirect(url_for('index', token=token))
    else:
        return render_template('token_page.html', token=None, mensaje="Por favor, conecte el USB")

if __name__ == '__main__':
    app.run(debug=True)
