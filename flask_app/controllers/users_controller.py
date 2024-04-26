from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.users import User
from flask_app.models.citas import Cita
from flask_app.models.servicios import Servicios
#Importamos BCrypt -> Encriptar la contraseña
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def go_login():
    return render_template("login.html")

@app.route("/registro")
def go_register():
    return render_template("registro.html")

@app.route("/register", methods =["post"])
def register():

    #Validar que la info sea correcta
    if not User.validate_user(request.form):
        return redirect("/registro")
    
    pass_encrypt = bcrypt.generate_password_hash(request.form['password'])
    form = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "telefono":request.form['telefono'],
        "email": request.form['email'],
        "password": pass_encrypt,
        "tipo_usuario": request.form['tipo_usuario']
    }

    nuevo_id = User.save(form) 
    session['user_id'] = nuevo_id
    return redirect("/dashboard_cliente")

@app.route("/dashboard_cliente")
def dashboard_cliente():
    if 'user_id' not in session:
        return redirect("/login")
    
    #Crear una instancia del usuario en base a la sesión
    form = {"id" : session["user_id"]}
    user = User.get_by_id(form)
    serv = Servicios.get_all()
    ap = Cita.get_by_userid(form)

    return render_template("dashboard_cliente.html", user=user, serv=serv, ap=ap)

@app.route("/dashboard_estilista")
def dashboard_estilista():
    if 'user_id' not in session:
        return redirect("/login")
    
    #Crear una instancia del usuario en base a la sesión
    form = {"id" : session["user_id"]}
    user = User.get_by_id(form)
    serv = Servicios.get_all()
    ap = Cita.get_all()

    return render_template("dashboard_estilista.html", user=user, serv=serv, ap=ap)

@app.route("/login", methods = ["post"])
def login():
    #Verificar que el correo exista en la bd
    user = User.get_by_email(request.form) 
    if not user:
        flash("Email no registrado", "login")
        return redirect("/login")
    
    #Si user si es instancia
    if not bcrypt.check_password_hash(user.password, request.form['password']): 
        flash("Contraseña incorrecta", "login")
        return redirect("/login")
    
    session['user_id'] = user.id #Guardando en sesión el id del usuario
    
    if user.tipo_usuario == 1:
        return redirect("/dashboard_estilista")

    if user.tipo_usuario == 2:
        return redirect("/dashboard_cliente")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
