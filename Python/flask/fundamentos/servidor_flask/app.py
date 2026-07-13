from flask import Flask
app = Flask(__name__)

# Ruta raíz - Página de inicio

@app.route("/")
def inicio():
    return "Bienvenido al servidor flask"

# Ruta genérica para explorar enrutamiento

@app.route("/explorar")
def explorar():
    return "¿Buscas algo? prueba con diferentes opciones"

# Rutas dinámicas para personalización

@app.route("/perfil/<nombre>")
def perfil(nombre):
    return f"Hola {nombre}, bienvenido a tu perfil"

# Ruta que repite un mensaje varias veces

@app.route("/repite/<mensaje>/<int:veces>")
def repetir(mensaje, veces):
    return f"¡repitiendo mensaje '{mensaje}'!" * veces

# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente

@app.errorhandler(404)
def error(error):
    return "¡ERROR: RUTA NO ENCONTRADA!"

# Ejecuta el servidor
if __name__ == "__main__":
   app.run(debug=True)