# ==========================================================
# SERVIDOR FLASK + MYSQL
# ==========================================================

from flask import Flask, render_template

from mascota import Mascota

from usuario import Usuario

# ==========================================================
# CREAR APLICACIÓN
# ==========================================================

app = Flask(__name__)

# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    """
    Consulta todas las mascotas de la base de datos
    y las envía hacia la plantilla HTML.
    """

    # ------------------------------------------------------
    # Consultar base de datos mediante el modelo.
    # ------------------------------------------------------

    mascotas = Mascota.get_all()


    # ------------------------------------------------------
    # Mostrar resultados en la terminal.
    # ------------------------------------------------------

    print(mascotas)


    # ------------------------------------------------------
    # Enviar resultados a Jinja2.
    # ------------------------------------------------------

    return render_template(
        "index.html",
        mascotas=mascotas
    )


@app.route("/usuarios")
def usuarios():
    """
    Consulta todos los usuarios de la base de datos
    y los envía hacia la plantilla HTML.
    """


    lista_usuarios = Usuario.get_all()


    return render_template(
        "usuarios.html",
        usuarios=lista_usuarios
    )


@app.route("/mascotas/<int:id>")
def detalle_mascota(id):
    """
    Consulta una mascota específica por su ID
    y la envía hacia la plantilla HTML.
    """


    mascota = Mascota.get_by_id(id)


    if not mascota:

        return "Mascota no encontrada", 404


    return render_template(
        "detalle_mascota.html",
        mascota=mascota
    )


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)