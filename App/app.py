from flask import Flask, render_template, request
from db import Database

db = Database()

app = Flask(__name__)

@app.route('/')
def index():
    data = []
    return render_template('index.html', data=data)

@app.route('/altausuario')
def altausuario():
    data = []
    return render_template('index.html', data=data)

#=========================PruebasDB===================================

#Seleccionar todos los combos 
@app.route('/pruebaCombo')
def pruebaCombo():
    data = db.query('''
                SELECT {} , {} FROM "combo";
            '''.format('"nombre"', '"total"'))
    print(data)
    return render_template('index.html', data=data)
    
#=========================Pruebas===================================



#Inicio de aplicacion
if __name__ == '__main__':
    app.run(debug=True)