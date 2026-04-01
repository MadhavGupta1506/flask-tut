from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, Wor d!</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
