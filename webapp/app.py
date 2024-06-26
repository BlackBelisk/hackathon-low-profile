from flask import Flask, render_template, request, redirect, url_for, jsonify
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
    devices = conectandoDispositivo.get_connected_devices()
    dev0 = devices[0]
    #dev1 = devices[1]
    LaTodopoderosa.hackear(dev0)

    # Procesar imagen y generar token.txt
    AUTH = "Amazon"
    return procesamientoImagen.procesarATexto(AUTH, "webapp/screen.png")


def obtener_token_desde_fono_foto():
    authenticator = "com.google.android.apps.authenticator2"
    cam1 = "com.motorola.camera3"
    cam2 = "com.android.camera"
    devices = conectandoDispositivo.get_connected_devices()
    dev1 = devices[0]
    dev0 = devices[1]
    intento.launch_app(authenticator, dev0)
    time.sleep(1)
    foto.take_photo(cam2, dev1)
    foto.get_photo(dev1)
    
    AUTH = "Amazon"
    
    return procesamientoImagen.procesarATexto(AUTH, "webapp/photo.png")


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
    #b = conectandoDispositivo.captura()
    if True:
        devices = conectandoDispositivo.get_connected_devices()
        dev0 = devices[0]
        android = intento.get_android_version(dev0)
        if int(android) <= 11:
            tok = obtener_token_desde_fono_screen()
        else:
            tok = obtener_token_desde_fono_foto()
            authenticator = "com.google.android.apps.authenticator2"
            intento.close_app(authenticator, dev0)
        #intento.close_app(cam, dev1)
        return jsonify(token=tok)
    else:
        return jsonify(error="Por favor, conecte el USB")

# Ruta para la página index
@app.route('/index')
def index():
    return render_template('index.html', mensaje="Gracias por ver")

if __name__ == '__main__':
    app.run(debug=False)