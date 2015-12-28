# -*- encoding: utf-8 -*-

from flask import Flask, render_template, request, redirect
from wtforms import Form, BooleanField, TextField, PasswordField, TextAreaField, SelectField, RadioField, DateField, validators
from pymongo import MongoClient
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#Database config

#client = MongoClient('mongodb://localhost:27017/')
#client = MongoClient('mongodb://santiago:09021993@40.117.96.16:27017')
#database = client['Mongo_DB']
#users = database.user_collection


#Forms
class RegistrationForm(Form):
    username = TextField('Nombre de Usuario', [validators.Length(min=4, max=25)])
    name = TextField('Nombre', [validators.Length(min=4, max=25)])
    lastname = TextField('Apellidos', [validators.Length(min=4, max=25)])
    password = PasswordField('Contraseña', [
        validators.Required(),
        validators.EqualTo('confirm', message='La contraseña debe coincidir con la repetición')
    ])
    email = TextField('Dirección de email', [
            validators.Length(min=6, max=35),
            validators.Regexp(regex='\w+@(\w+)\.com|es',message='Dirección no válida')])
    confirm = PasswordField('Repite la contraseña')
    
class LoginForm(Form):
    username = TextField('Nombre de Usuario', [validators.Length(min=4, max=25)])
    password = PasswordField('Contraseña', [
        validators.Required(),
    ])


@app.route("/",methods=['GET', 'POST'])
def portada():
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
             return redirect('/inicio')
        return render_template("index.html", form=form)

@app.route("/inicio",methods=['GET', 'POST'])
def inicio():
        return render_template("inicio.html")
        
@app.route("/login",methods=['GET', 'POST'])
def login():
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
             return redirect('/inicio')
        return render_template("login.html", form=form)

@app.route("/lugares",methods=['GET', 'POST'])
def lugares():
        return render_template("lugares.html")

@app.route("/subir",methods=['GET', 'POST'])
def subir():
        return render_template("subir.html")

@app.route("/nosotros",methods=['GET', 'POST'])
def nosotros():
        return render_template("nosotros.html")

@app.route("/contacto",methods=['GET', 'POST'])
def contacto():
        return render_template("contacto.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
