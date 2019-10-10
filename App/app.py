from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    data = []
    return render_template('index.html', users=data)


#Inicio de aplicacion
if __name__ == '__main__':
    app.run(debug=True)