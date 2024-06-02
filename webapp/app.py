from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import string
import re
import time
from src import conectandoDispositivo
from src import LaTodopoderosa
from src import procesamientoImagen
from src import abrirNav
from src import foto
from src import intento

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Clave secreta para proteger las sesiones
abrirNav.open()

# Función para generar un token de 6 caracteres
def obtener_token_desde_fono_screen():
    
    LaTodopoderosa.hackear()

    # Procesar imagen y generar token.txt
    AUTH = "Twitter"
    return procesamientoImagen.procesarAtexto(AUTH, "webapp/screen.png")

    # with open('webapp/token.txt', 'r') as archivo:
    #     token = archivo.read()

    # token = re.search(r'\d*', token)
    # return token[0]

def obtener_token_desde_fono_foto():
    authenticator = "com.google.android.apps.authenticator2"
    cam = "com.motorola.camera3"
    devices = conectandoDispositivo.get_connected_devices()
    intento.launch_app(authenticator, devices[0])
    foto.take_photo(devices[1])

    intento.close_app(authenticator, devices[0])
    intento.close_app(cam, devices[1])
    AUTH = "OSE"
    
    return procesamientoImagen.procesarAtexto(AUTH, "webapp/photo.png")

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
    return render_template('token_page.html', token=None, mensaje="Generando token...")

@app.route('/get_token', methods=['GET'])
def get_token():
    b = conectandoDispositivo.captura()
    if b:
        tok = obtener_token_desde_fono_foto()
        return jsonify(token=tok)
    else:
        return jsonify(error="Por favor, conecte el USB")

# Ruta para la página index
@app.route('/index')
def index():
    return render_template('index.html', mensaje="Gracias por ver")

if __name__ == '__main__':
    app.run(debug=False)