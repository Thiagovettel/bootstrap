from flask import Flask,template_rendered,request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Ola Mundo'

if __name__ == '__main__':
    app.run(debug=True)