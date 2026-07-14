from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():

    return render_template(

        "index.html",

        nombre="Fabrizio",

        curso="Desarrollo Web con Flask",

        ciudad="Santiago",

        profesor=False,

        anio=2026,

        tecnologias=[
        "Python",
        "Flask",
        "HTML",
        "CSS"

    ]
)


@app.route("/jugadores")
def jugadores():
 return render_template(

    "jugadores.html",

    jugador="XxWbdsxX",

    puntaje=50000,

    lider=True

)

if __name__ == "__main__":

    app.run(debug=True)