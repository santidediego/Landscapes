# -*- encoding: utf-8 -*-

from flask import Flask, render_template, request, redirect
from wtforms import Form, BooleanField, TextField, PasswordField, TextAreaField, SelectField, RadioField, DateField, validators
#from pymongo import MongoClient

#client = MongoClient('mongodb://localhost:27017/')
app = Flask(__name__)
#db=client['users_database']
#collection = db.user_collection

class RegistrationForm(Form):
    username = TextField('Nombre de Usuario', [validators.Length(min=4, max=25)])
    password = PasswordField('Contraseña', [
        validators.Required(),
        validators.EqualTo('confirm', message='La contraseña debe coincidir con la repetición')
    ])
    confirm = PasswordField('Repite la contraseña')


@app.route("/",methods=['GET', 'POST'])
def login():
        return render_template("index.html")

@app.route("/inicio",methods=['GET', 'POST'])
def inicio():
        return render_template("inicio.html")

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
