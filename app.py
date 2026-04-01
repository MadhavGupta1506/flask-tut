from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, Wor d!</h1>"
@app.route('/greet/<name>')
def greet(name  ):
    return f"<h1>Hello {name}!</h1>"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"<h1>{a} + {b} = {a + b}</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
