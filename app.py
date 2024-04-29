from flask import Flask, render_template, request, redirect, session
from db import Database
import api

app = Flask(__name__)
dbo= Database()

@app.route('/')
def index():
    # session['logged_in'] = 0
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
        session['logged_in']=1
        return redirect('/profile')
    else:
        return render_template('login.html', message="Email/Password did not match",  message_type="error")



@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')


@app.route('/sentiment')
def sentiment():
    if session:
        return render_template('sentiment.html')
    else:
        return redirect('/')

@app.route('/perform_sentiment', methods=['post'])
def perform_sentiment():
    if session:
            text=request.form.get('text')
            response=api.sentiment(text)
            return render_template('sentiment.html',response=response)
    else:
        return redirect('/')


app.run(debug=True)#so that we dont have o refresh multiple time
