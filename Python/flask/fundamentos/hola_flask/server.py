from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola Mundo!"

@app.route("/Nosotros")
def nosotros():
    return "Conocenos"

#Productos

@app.route("/Productos")
def Productos():
    return "Ventas"

#Contacto

@app.route("/Contacto")
def Contactos():
    return "Contacto"

if __name__ == "__main__":
    app.run(debug=True)