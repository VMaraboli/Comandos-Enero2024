from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime 

class Cita:

    def __init__(self,data):
        self.id = data['id']
        self.estado = data['estado']
        self.fecha = data['fecha']
        self.hora = data['hora']
        self.user_name = data['user_id']
        self.servicio = data['servicio_id']
        
        self.nombre_usuario = data['nombre_usuario']
        self.nombre_servicio = data['nombre_servicio']
        self.valor_servicio = data['valor_servicio']
        
    @staticmethod
    def validate_cita(form):
        is_valid = True

        if form['servicio_id'] == '':
            flash('Debes seleccionar un estado', 'cita')
            is_valid = False

        fecha_obj = datetime.strptime(form["fecha"], "%Y-%m-%d")
        if fecha_obj.isoweekday() in range (6,8):
            flash('Debes seleccionar de lunes a viernes', 'cita')
            is_valid = False

        if form['fecha'] == '':
            flash('Ingrese una fecha', 'cita')
            is_valid = False
        else:
            fecha = datetime.strptime(form['fecha'], '%Y-%m-%d') 
            hoy = datetime.now() 
            if hoy > fecha:
                flash('La fecha no puede ser anterior a la actual', 'cita')
                is_valid = False

        if form['hora'] == '':
            flash('Ingrese una hora', 'cita')
            is_valid = False
        
        query = "SELECT * FROM citas WHERE fecha = %(fecha)s and hora=%(hora)s"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)

        if len(result) >=1:
            flash("El horario no se encuentra disponible", "cita")
            is_valid = False

        return is_valid
        
    @classmethod
    def save(cls,form):
        query = "INSERT INTO citas (estado, fecha, hora, user_id, servicio_id) VALUES (%(estado)s, %(fecha)s, %(hora)s, %(user_id)s, %(servicio_id)s)"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT citas.*, usuarios.nombre as nombre_usuario, servicios.nombre_servicio as nombre_servicio, servicios.valor as valor_servicio FROM citas JOIN usuarios ON citas.user_id = usuarios.id JOIN servicios ON citas.servicio_id = servicios.id"
        results = connectToMySQL('esquema_proyecto_individual').query_db(query)
        apms = []
        for r in results:
            apms.append(cls(r))
        
        return apms

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT citas.*, usuarios.nombre as nombre_usuario, servicios.nombre_servicio as nombre_servicio, servicios.valor as valor_servicio FROM citas JOIN usuarios ON citas.user_id = usuarios.id JOIN servicios ON citas.servicio_id = servicios.id WHERE citas.id = %(id)s"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, data) 
        apm = cls(result[0])
        return apm
    
    @classmethod
    def get_by_userid(cls, form):
        query = "SELECT citas.*, usuarios.nombre as nombre_usuario, servicios.nombre_servicio as nombre_servicio, servicios.valor as valor_servicio FROM citas JOIN usuarios ON citas.user_id = usuarios.id JOIN servicios ON citas.servicio_id = servicios.id WHERE citas.user_id = %(id)s"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form) 
        apms = []
        for r in result:
            apms.append(cls(r))        
        return apms

    @classmethod
    def update(cls, form):
        query = "UPDATE citas SET fecha=%(fecha)s, hora=%(hora)s,servicio_id=%(servicio_id)s WHERE id=%(id)s" 
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)
        return result

    @classmethod
    def update_finalizada(cls, form):
        query = "UPDATE citas SET estado='Finalizada' WHERE id=%(id)s" 
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)
        return result
    
    @classmethod
    def update_ausente(cls, form):
        query = "UPDATE citas SET estado='Ausente' WHERE id=%(id)s" 
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)
        return result
    
    
    @classmethod
    def delete(cls, form):
        query = "DELETE FROM citas WHERE id = %(id)s"
        result = connectToMySQL('esquema_proyecto_individual').query_db(query, form)
        return result
