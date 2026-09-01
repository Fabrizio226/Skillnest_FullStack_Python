from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# La clave secreta es necesaria para poder usar sesiones
app.secret_key = 'si' 

@app.route('/')
def inicio():
    # Comprobarvisitas
    if 'visitas' in session:
        session['visitas'] += 1
    else:
        session['visitas'] = 1

    # Comprobar reinicios
    if 'reinicios' not in session:
        session['reinicios'] = 0

    return render_template('index.html')

@app.route('/sumar_dos')
def sumar_dos():
    if 'visitas' in session:
        session['visitas'] += 1
    return redirect('/')

@app.route('/incrementar_personalizado', methods=['POST'])
def incrementar_personalizado():
    num = int(request.form['numero'])
    if 'visitas' in session:
        session['visitas'] += (num - 1)
    return redirect('/')

@app.route('/reiniciar')
def reiniciar():
    if 'reinicios' in session:
        session['reinicios'] += 1
    else:
        session['reinicios'] = 1
        
    session['visitas'] = 0  # Se reincia el contador de visitas
    return redirect('/')

@app.route('/destruir_sesion')
def destruir_sesion():
    session.clear() # Elimina todos los datos de la sesión
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)