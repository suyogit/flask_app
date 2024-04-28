from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')

app.run(debug=True)#so that we dont have o refresh multiple time
