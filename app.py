from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=[])
def login():
    pass

if __name__ == '__main__':
   app.run(debug=app.config['DEBUG'])