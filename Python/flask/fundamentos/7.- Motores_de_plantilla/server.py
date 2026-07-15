from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template(

        "index.html",

        nombre="Fabrizio",
        apellido="Ortiz",
        curso="4° Programación",
        institucion="Liceo Comercial Vate Vicente Huidobro",
        anio=2026,
        es_docente= False,  #Con true cambia el mensjae
        tecnologias=[
            "Python",
            "Flask",
            "HTML",
            "CSS",
            "JavaScript"
        ]
    )


if __name__ == "__main__":
    app.run(debug=True)