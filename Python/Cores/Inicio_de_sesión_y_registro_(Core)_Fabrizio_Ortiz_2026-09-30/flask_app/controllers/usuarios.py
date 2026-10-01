from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not Usuario.validar_registro(request.form):
        return redirect('/')

    hashed_password = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': hashed_password,
        'fecha_nacimiento': request.form.get('fecha_nacimiento') or None
    }

    usuario_id = Usuario.guardar(data)
    session['usuario_id'] = usuario_id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    usuario = Usuario.obtener_por_email(request.form['email'])
    if not usuario:
        flash("Credenciales inválidas.", "login")
        return redirect('/')

    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Credenciales inválidas.", "login")
        return redirect('/')

    session['usuario_id'] = usuario.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')

    usuario = Usuario.obtener_por_id(session['usuario_id'])
    if not usuario:
        session.clear()
        return redirect('/')

    return render_template('dashboard.html', usuario=usuario)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')