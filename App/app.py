from flask import Flask, render_template, request
from db import Database
from modelos.usuario import Usuario

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

#====ROL
@app.route('/altaRol')
def altaRol():
     return render_template('pruebaDB/altaRol.html') 

@app.route('/guardarRol', methods=["POST"])
def guardarRol():
    if request.method == 'POST':
        nombre = request.form['nombreRol']
        print(nombre)  
        data = db.queryInsert('''
               INSERT INTO "rol" ("nombreRol") values ('{}');
            '''.format(nombre))
   
    return render_template('pruebaDB/rolGuardado.html', data=data)  

@app.route('/bajaRol') 
def bajaRol():
    return render_template('pruebaDB/bajaRol.html')  

@app.route('/eliminarRol', methods=["POST"])
def eliminarRol():
    if request.method == 'POST':
        nombre = request.form['nombreRol']
        print(nombre)  
        data = db.queryInsert('''
               DELETE FROM "rol" WHERE "nombreRol" = '{}'; 
            '''.format(nombre))

    return render_template('pruebaDB/rolEliminado.html', data=data)    

@app.route('/modificarRol') 
def modificarRol():
    return render_template('pruebaDB/modificarRol.html')  

@app.route('/editarRol', methods=["POST"])
def editarRol():
    if request.method == 'POST':
        nombre = request.form['nombreRol']
        nombreNuevo = request.form['nombreNuevoRol']
        print(nombre)  
        data = db.queryInsert('''
               UPDATE "rol"
	                SET "nombreRol" = '{}'
	                WHERE "nombreRol" = '{}';
            '''.format(nombreNuevo, nombre))

    return render_template('pruebaDB/rolModificado.html', data=data)
#===========FIN ROL


@app.route('/altaUsuario')
def altaUsuario():
    #data = db.query('''
    #           SELECT {} , {} FROM "combo";
     #       '''.format('"nombre"', '"total"'))
   # print(data)
    return render_template('pruebaDB/altaUsuario.html')    
    
#=========================Pruebas===================================



#Inicio de aplicacion
if __name__ == '__main__':
    app.run(debug=True)