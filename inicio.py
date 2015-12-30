# -*- encoding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, flash
from wtforms import Form, BooleanField, TextField, PasswordField, TextAreaField, SelectField, RadioField, DateField, validators
from pymongo import MongoClient
from flask.ext.login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import check_password_hash


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'



#Database config
WTF_CSRF_ENABLED = True
#client = MongoClient('mongodb://localhost:27017/')
client = MongoClient('mongodb://mongouser:09021993@40.117.96.16:27017')
database = client['Mongo_DB']
USER_COLLECTION = database.users
DEBUG = True


#Users config


class User():

    def __init__(self, username):
        self.username = username
        self.email = None

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(pass1, pass2):
        return pass1==pass2
        #return check_password_hash(password_hash, password)


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
        validators.Required()
    ])

def guardar_datos(form):
    USER_COLLECTION.insert({"_id": str(form.username.data),
                            "_password": str(form.password.data),
                            "_lastname": str(form.lastname.data),
                            "_name": str(form.name.data),
                            "_email": str(form.email.data)
                            })

@app.route("/",methods=['GET', 'POST'])
def portada():
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
             return redirect('/inicio')
        return render_template("index.html", form=form)

@app.route("/registro",methods=['GET', 'POST'])
def register():
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
             guardar_datos(form)
             return redirect('/login')
        return render_template("registro.html", form=form)

@app.route("/login",methods=['GET', 'POST'])
def login():
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
                print("Pasa1")
                user = USER_COLLECTION.find_one({"_id": form.username.data})
                print(user)
                if user and User.validate_login(user['_password'], form.password.data):
                    print("Pasa3")
                    user_obj = User(user['_id'])
                    login_user(user_obj)
                    flash("Correcto!", category='success')
                    print("Pasa4")
                    return redirect('/inicio') #Hay que retocarlo, hay que usar la utilidad next que aparece en el tutorial
                print("Pasa5")
                flash("Nombre de usuario o contraseña erróneos!") #No hace nada, comprobar
                print("Pasa6")
        return render_template("login.html", form=form)


@app.route("/inicio",methods=['GET', 'POST'])
@login_required
def inicio():
        return render_template("inicio.html")

@app.route("/lugares",methods=['GET', 'POST'])
@login_required
def lugares():
        return render_template("lugares.html")

@app.route("/subir",methods=['GET', 'POST'])
@login_required
def subir():
        return render_template("subir.html")

@app.route("/nosotros",methods=['GET', 'POST'])
@login_required
def nosotros():
        return render_template("nosotros.html")

@app.route("/contacto",methods=['GET', 'POST'])
@login_required
def contacto():
        return render_template("contacto.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



@lm.user_loader
def load_user(username):
    u = USER_COLLECTION.find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])



if __name__ == "__main__":
    app.run(host='0.0.0.0')
