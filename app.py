from flask import Flask, render_template, request
from db import Database

app = Flask(__name__)
dbo= Database()

@app.route('/')
def index():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name= request.form.get('name')
    email=request.form.get('email')
    password= request.form.get('password')
    response=dbo.insert(name, email, password)
    if response:
        return render_template('login.html', message="Registration Successful, kindly login to proceed", message_type="success")
    else:
        return render_template('register.html', message="Email already exists!")

@app.route('/perform_login',methods=['post'])
def perform_login():
    email=request.form.get('email')
    password= request.form.get('password')
    response=dbo.validate( email, password)
    if response:
        return "welcome" #menu here
    else:
        return render_template('login.html', message="Email/Password did not match",  message_type="error")





app.run(debug=True)#so that we dont have o refresh multiple time
