from flask import Flask, render_template, request, redirect
from wtforms import Form, BooleanField, TextField, PasswordField, TextAreaField, SelectField, RadioField, DateField, validators
app = Flask(__name__)

class RegistrationForm(Form):
    username = TextField('Nombre de Usuario', [validators.Length(min=4, max=25)])
    password = PasswordField('Contraseña', [
        validators.Required(),
        validators.EqualTo('confirm', message='La contraseña debe coincidir con la repetición')
    ])
    confirm = PasswordField('Repite la contraseña')


@app.route("/",methods=['GET', 'POST'])
def hello():
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
            return('¡Gracias %s por registrarte!' % form.username.data)
        return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run()
