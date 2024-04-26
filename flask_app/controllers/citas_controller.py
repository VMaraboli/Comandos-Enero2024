from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.users import User
from flask_app.models.citas import Cita
from flask_app.models.servicios import Servicios


@app.route('/agregar_cita')
def nueva_cita():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    form = {"id" : session["user_id"]}
    user = User.get_by_id(form)
    serv = Servicios.get_all() 
    return render_template('agregar_cita.html',serv=serv, user=user)

@app.route('/create/cita', methods=['POST'])
def crear_cita():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #Validar la Calificación
    if not Cita.validate_cita(request.form):
        return redirect('/agregar_cita')
    
    #Guardar la Calificación
    Cita.save(request.form)

    return redirect('/dashboard_cliente')

#UPDATE

@app.route('/citas/<int:id>') 
def editar_cita(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #Buscar la instancia de Grade que corresponde al ID
    diccionario = {"id": id}
    ap = Cita.get_by_id(diccionario)
    serv     = Servicios.get_all()

    return render_template('editar_cita.html', ap=ap, serv=serv)

@app.route('/update/cita', methods=['post'])
def update_cita():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    
    #Validar que el formulario sea correcto
    if not Cita.validate_cita(request.form):
        return redirect('/citas/'+request.form['id'])
    
    #Actualizar el registro
    Cita.update(request.form)
    
    return redirect("/dashboard_cliente")


# DELETE

@app.route('/delete/<int:id>')
def delete_cita(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/login')
    
    #Borrar
    form = {"id": id}
    Cita.delete(form)
    
    return redirect("/dashboard_cliente")

@app.route('/citas/ausente/<int:id>')
def ausente(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/login')
    
    #Borrar
    form = {"id": id}
    Cita.update_ausente(form)
    
    return redirect("/dashboard_estilista")
    
    
@app.route('/citas/completa/<int:id>')
def completa(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash('Favor iniciar sesión', 'not_in_session')
        return redirect('/login')
        
    form = {"id": id}
    Cita.update_finalizada(form)

    return redirect("/dashboard_estilista")
    