#pipenv install flask pymysql flask-bcrypt
#importación de app
from flask_app import app

#importación de controladores
from flask_app.controllers import users_controller, citas_controller, servicios_controller

#Ejecución app
if __name__ == "__main__":
    app.run(debug=True)