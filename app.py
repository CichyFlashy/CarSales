from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WSXedc1234'

class RegistrationForm(FlaskForm):
    name = StringField('User name')
    last_name = StringField('User last name')
    email = EmailField('User e-mail')
    password = PasswordField('User password')
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kontakt')
def contact():
    return render_template('contact.html')

@app.route('/o-nas')
def about():
    return render_template('about.html')

@app.route('/uslugi/naprawa')
def fix():
    return render_template('fix.html')

@app.route('/uslugi/komis')
def dealership():
    return render_template('dealership.html')

@app.route('/uslugi/czesci')
def parts():
    return render_template('parts.html')

@app.route('/uslugi/detailing')
def detailing():
    return render_template('detailing.html')

@app.route('/registration')
def registration():
    form = RegistrationForm()
    return render_template('/registration.html', form=form)

if __name__ == "__main__":
    app.run()