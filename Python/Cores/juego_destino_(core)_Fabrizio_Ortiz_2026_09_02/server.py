from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "clave_secreta_destino"

PREDICCIONES = [
    "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
    "Un viaje inesperado cambiará el rumbo de tus proyectos de forma positiva.",
    "Pronto recibirás una noticia sobre tus finanzas que te traerá gran paz mental.",
    "Una antigua amistad regresará a tu vida para ofrecerte una gran oportunidad."
]

# Ojala las predicciones sean acertadas

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    session["nombre"] = request.form.get("nombre")
    session["edad"] = request.form.get("edad")
    session["color"] = request.form.get("color")
    session["animal"] = request.form.get("animal")
    
    # Generar predicción y número de la suerte aleatorio (1-100)
    session["prediccion"] = random.choice(PREDICCIONES)
    session["numero_suerte"] = random.randint(1, 100)
    
    return redirect("/futuro")

@app.route("/futuro")
def futuro():
    if "nombre" not in session:
        return redirect("/")
    return render_template("futuro.html")

if __name__ == "__main__":
    app.run(debug=True)