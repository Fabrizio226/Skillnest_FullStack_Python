# ==========================================
# IMPORTACIONES
# ==========================================
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    """Muestra el formulario para registrar un producto."""
    return render_template("index.html")


@app.route("/registrar", methods=["POST"])
def registrar():
    """
    Recibe los datos del producto vía POST, 
    imprime la información en consola y redirige.
    """
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    print("============================")
    print("Producto recibido")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print(f"Categoría: {categoria}")
    print("============================")

    return redirect(url_for("resultado"))

@app.route("/resultado")
def resultado():
    """Muestra la confirmación del registro tras la redirección."""
    return render_template("resultado.html")

@app.route("/ayuda")
def ayuda():
    """Explica los conceptos clave de POST, GET, redirect y request.form."""
    return render_template("ayuda.html")

# ==========================================
# EJECUTAR SERVIDOR
# ==========================================
if __name__ == "__main__":
    app.run(debug=True)