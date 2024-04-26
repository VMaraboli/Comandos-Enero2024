from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re #importar expresiones regulares
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email

class Servicios:

    def __init__(self,data):
        self.id = data['id']
        self.nombre_servicio = data['nombre_servicio']
        self.valor = data["valor"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,form):
        query = "INSERT INTO servicios (nombre_servicio, valor) VALUES (%(nombre_servicio)s, %(valor)s)"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)
        return result
    
    @staticmethod
    def validate_service(form):
        is_valid = True

        if len(form["nombre_servicio"] )< 5:
            flash("Nombre de servicio debe tener al menos 5 carcteres","servicio")
            is_valid = False
        
        if len(form["valor"])<4:
            flash("el valor debe tener al menos 4 dígitos","servicio")
            is_valid = False

        return is_valid
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM servicios ORDER BY valor ASC"
        results = connectToMySQL('esquema_proyecto_individual').query_db(query)
        servicio = []
        for s in results:
            servicio.append(cls(s))
        
        return servicio

    @classmethod
    def get_by_id(cls, form):
        query = "SELECT * FROM servicios WHERE id = %(id)s"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form) 
        servicio = cls(result[0])
        return servicio

    @classmethod
    def update(cls, form):
        query = "UPDATE servicios SET valor=%(valor)s WHERE id=%(id)s"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls, form):
        query = "DELETE FROM servicios WHERE id = %(id)s"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)
        return result
