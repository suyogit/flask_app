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
        return "Registration Successful"
    else:
       return "Email already exists."




app.run(debug=True)#so that we dont have o refresh multiple time
