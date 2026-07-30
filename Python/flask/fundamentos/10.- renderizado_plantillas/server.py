from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/listas")
def renderizar_listas():

    # Lista de números

    numeros = [7, 15, 22]

    # Lista de diccionarios

    listado_estudiantes = [

        {
            "nombre":"Florencia",
            "edad":25
        },

        {
            "nombre":"Valentina",
            "edad":30
        },

        {
            "nombre":"José",
            "edad":27
        },

        {
            "nombre":"Patricio",
            "edad":21
        }

    ]

    return render_template(

        "listas.html",

        numeros=numeros,

        estudiantes=listado_estudiantes

    )

@app.route("/videojuegos")
def videojuegos():

    listado_videojuegos = [

    {
    "nombre":"Geometry Dash",
    "plataforma":"PC, Celulares",
    "anio": 2003
    },

    {
    "nombre":"Super Mario 3D World",
    "plataforma":"Wii U",
    "anio":2013
    },

    {
    "nombre":"Mario & Luigi: Superstar Saga",
    "plataforma":"Game Boy Advance",
    "anio":2003
        
    },

    {
    "nombre":"Assassin's Creed IV: Black Flag",
    "plataforma":"PC, PlayStation 4, Nintendo Switch",
    "anio":2011
    },
    {
    "nombre":"Osu!",
    "plataforma":"PC",
    "anio":2007
    },

    {
    "nombre":"Pizza Tower",
    "plataforma":"PC, Nintendo Switch",
    "anio":2023
    }
    ]

    return render_template(

        "videojuegos.html",

        videojuegos=listado_videojuegos

    )


if __name__ == "__main__":
   app.run(debug=True)