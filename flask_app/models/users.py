from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re #importar expresiones regulares
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email

class User:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.telefono = data['telefono']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.tipo_usuario = data['tipo_usuario']

    @classmethod
    def save(cls, form):
        query = "INSERT INTO usuarios(nombre, apellido, telefono, email, password, tipo_usuario) VALUES(%(nombre)s, %(apellido)s, %(telefono)s,%(email)s, %(password)s, %(tipo_usuario)s)"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form) 
        return result

    @staticmethod
    def validate_user(form):
        is_valid = True

        if len(form["nombre"] )< 2:
            flash("Nombre debe tener al menos 2 carcteres","register")
            is_valid = False
        
        if len(form["apellido"])<2:
            flash("Apellido debe tener al menos 2 caracteres","register")
            is_valid = False

        if len(form["telefono"]) == 10:
            flash("Tu N° telefono debe tener 9 digitos","register")
            is_valid = False

        if not EMAIL_REGEX.match(form["email"]):
            flash("E-mail inválido", "register")
            is_valid = False

        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)

        if len(result) >=1:
            flash("E-mail ya se encuentra registrado", "register")
            is_valid = False

        if len(form["password"] )< 6:
            flash("La contraseña debe tener al menos 6 caracteres", "register")
            is_valid = False

        if form["password"] != form["confirm"]:
            flash("Las contraseñas no coinciden", "register")
            is_valid = False

        return is_valid

    @classmethod
    def get_by_email(cls,form):
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)
        if len(result) == 1:
            #Si existe el usuario, me regresa solo un registro
            user =  cls(result[0])
            return user #Regreso la instancia del usuario con ese correo
        else:
            return False
        
    @classmethod
    def get_by_id(cls,form):
        query = "SELECT * FROM usuarios WHERE id=%(id)s"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)
        user =  cls(result[0])
        return user
    
    @classmethod
    def get_tipo_cliente(cls,form):
        query = "SELECT tipo_usuario FROM usuarios WHERE tipo_cliente=%(tipo_cliente)s"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)
        user =  cls(result[0])
        return user