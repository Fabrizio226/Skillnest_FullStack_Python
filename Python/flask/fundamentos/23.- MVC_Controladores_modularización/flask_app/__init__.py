# ==========================================================
# INICIALIZACIÓN DE LA APLICACIÓN FLASK
# ==========================================================

from flask import Flask


# ==========================================================
# CREAR INSTANCIA DE FLASK
# ==========================================================

app = Flask(__name__)


# ==========================================================
# SECRET KEY
# ==========================================================
#
# Necesaria para funcionalidades como:
#
# - session
# - flash
#
# Aunque actualmente no necesitamos ambas obligatoriamente,
# dejamos la configuración preparada para la aplicación.
#

from flask import Flask

app = Flask(__name__, template_folder='../templates')
app.secret_key = "keep_it_secret_keep_it_safe"


# En un proyecto real esta clave debería mantenerse fuera
# del código utilizando variables de entorno.
# ==========================================================

app.secret_key = "clave-secreta-desarrollo"
