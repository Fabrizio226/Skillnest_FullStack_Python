from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():

    return render_template(

        "index.html",

        nombre="Fabrizio",

        apellido="",

        curso="",

        institucion="",

        profesor=False,

        anio=2026,

lenguajes = [

    "Python",

    "Flask",

    "HTML",

    "CSS",

    "JavaScript"

]
)