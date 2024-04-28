from flask import Flask, render_template, request

app = Flask(__name__)

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

    return name + " "+ email+ " " + password



app.run(debug=True)#so that we dont have o refresh multiple time
