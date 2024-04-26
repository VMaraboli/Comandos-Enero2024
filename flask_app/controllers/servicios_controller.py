from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.users import User
from flask_app.models.citas import Cita
from flask_app.models.servicios import Servicios

#Agregar servicio
@app.route('/agregar_servicio')
def nuevo_servicio():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    return render_template('agregar_servicio.html')

@app.route('/create/servicio', methods=['POST'])
def crear_servicio():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #Validar la Calificación
    if not Servicios.validate_service(request.form):
        return redirect('/agregar_servicio')
    
    #Guardar la Calificación
    Servicios.save(request.form)

    return redirect('/dashboard_estilista')

#Actualizar
@app.route('/servicio/<int:id>') 
def editar_servicio(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #Buscar la instancia de Grade que corresponde al ID
    diccionario = {"id": id}
    serv = Servicios.get_by_id(diccionario)

    return render_template('editar_servicio.html', serv=serv)

@app.route('/update/servicio', methods=['post'])
def update_servicio():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #Validar que el formulario sea correcto
    if not Servicios.validate_service(request.form):
        return redirect('/servicio/'+request.form['id'])
    
    #Actualizar el registro
    Servicios.update(request.form)
    return redirect('/dashboard_estilista')

# DELETE

@app.route('/delete/servicio/<int:id>')
def delete_servicio(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #Borrar
    form = {"id": id}
    Servicios.delete(form)

    return redirect('/dashboard_estilista')