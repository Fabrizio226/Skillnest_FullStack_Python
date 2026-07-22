from flask import Flask, render_template

app = Flask(__name__)

# Datos de jugadores con puntajes
jugadores = [
   {"nombre": "AlexGamer", "puntaje": 5000},
   {"nombre": "PixelMaster", "puntaje": 7500},
   {"nombre": "ShadowNinja", "puntaje": 8200},
   {"nombre": "CyberWarrior", "puntaje": 9100},
   {"nombre": "UltraNoob", "puntaje": 3000}
]


# Ruta para mostrar el ranking de jugadores
@app.route("/ranking")
def ranking():
    return render_template(
        "ranking.html",
        jugadores=jugadores
    )


# Ruta para mostrar un número limitado de jugadores
@app.route("/ranking/<int:limite>")
def ranking_limitado(limite):
    return render_template(
        "ranking.html",
        jugadores=jugadores[:limite]
    )


# Ruta para personalizar el color del ranking
@app.route("/ranking/<int:limite>/<string:color>")
def ranking_color(limite, color):
    return render_template(
        "ranking.html",
        jugadores=jugadores[:limite],
        color=color
    )


# Ejecutar el servidor
if __name__ == "__main__":
   app.run(debug=True)