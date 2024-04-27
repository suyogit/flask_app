from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1 style='color:green'>Hellow suyog</h1>"

app.run(debug=True)#so that we dont have o refresh multiple time
