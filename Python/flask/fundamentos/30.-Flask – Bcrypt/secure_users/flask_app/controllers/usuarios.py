from flask import render_template, redirect, request, session, flash
from flask_app import app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_app.models.usuario import Usuario

# 1. Mostrar formulario de Login (reemplaza index.html)
@app.route('/')
@app.route('/login')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('login.html')

# 2. Mostrar formulario de Registro
@app.route('/registro', methods=['GET'])
def vista_registro():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('registro.html')

# 3. Procesar el formulario de Registro (POST)
@app.route('/registro', methods=['POST'])
def registrar():
    password_hash = generate_password_hash(request.form['password'])
    data = {
        "nombre": request.form['nombre'],
        "email": request.form['email'],
        "password": password_hash
    }
    user_id = Usuario.guardar(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

# 4. Procesar el inicio de sesión (POST)
@app.route('/login', methods=['POST'])
def login():
    usuario = Usuario.obtener_por_email({"email": request.form['email']})
    if not usuario:
        flash("Correo no registrado", "login")
        return redirect('/login')
        
    if not check_password_hash(usuario.password, request.form['password']):
        flash("Contraseña incorrecta", "login")
        return redirect('/login')
        
    session['user_id'] = usuario.id
    return redirect('/dashboard')

# 5. Vista del Panel
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    usuario = Usuario.obtener_por_id({"id": session['user_id']})
    return render_template('dashboard.html', usuario=usuario)

# 6. Cerrar sesión
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')