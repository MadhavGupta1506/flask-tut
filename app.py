from flask import Flask, render_template, request 

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    myval="Hello, Flask!"
    myres=54
    mylist=[1,2,3,4,5]
    return render_template('index.html', myval=myval, myres=myres, mylist=mylist)

@app.route('/myhtml')
def show_myhtml():
    return render_template('myhtml.html',some_text="This is some text passed to the template")

@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

@app.route('/greet/<name>')
def greet(name  ):
    return f"<h1>Hello {name}!</h1>"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"<h1>{a} + {b} = {a + b}</h1>"

@app.route("/hello")
def hello():
    return "Hello, World!\n" ,200
    1

 
@app.route('/query')
def query():
    return f"<h1>Query parameters: {request.args}</h1>"
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
