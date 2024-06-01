from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import string

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Clave secreta para proteger las sesiones

# Función para generar un token de 6 caracteres
def generate_token(length=6):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

# Ruta para el formulario de inicio de sesión
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Verificar las credenciales de inicio de sesión (aquí debes agregar tu lógica de autenticación)
        # Por ejemplo, si las credenciales son válidas, podrías redirigir al usuario a la página del token
        # Aquí simplemente redirigimos al usuario a la página del token
        return redirect(url_for('token_page'))
    return render_template('login.html')

# Ruta para la página del token generado
@app.route('/token_page')
def token_page():
    token = generate_token()
    return render_template('token_page.html', token=token)

if __name__ == '__main__':
    app.run(debug=True)
