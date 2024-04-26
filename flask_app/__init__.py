#Importación de flask
from flask import Flask

#Inicialización de la app
app = Flask(__name__)

#Declaramos la clave secreta
app.secret_key = "llave secreta"