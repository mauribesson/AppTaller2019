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
    data = db.querySelect('''
                SELECT {} , {} FROM "combo";
            '''.format('"nombre"', '"total"'))
    print(data)
    return render_template('index.html', data=data)

#====ROL
@app.route('/altaRol')
def altaRol():
     return render_template('rol/altaRol.html') 

@app.route('/guardarRol', methods=["POST"])
def guardarRol():
    if request.method == 'POST':
        nombre = request.form['nombreRol']
        print(nombre)  
        data = db.queryInsert('''
               INSERT INTO "rol" ("nombreRol") values ('{}');
            '''.format(nombre))
   
    return render_template('rol/rolGuardado.html', data=data)  

@app.route('/bajaRol') 
def bajaRol():
    return render_template('rol/bajaRol.html')  

@app.route('/eliminarRol', methods=["POST"])
def eliminarRol():
    if request.method == 'POST':
        nombre = request.form['nombreRol']
        print(nombre)  
        data = db.queryInsert('''
               DELETE FROM "rol" WHERE "nombreRol" = '{}'; 
            '''.format(nombre))

    return render_template('rol/rolEliminado.html', data=data)    

@app.route('/modificarRol') 
def modificarRol():
    return render_template('rol/modificarRol.html')  

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

    return render_template('rol/rolModificado.html', data=data)

@app.route('/listarRol')
def listarRol():
    data = db.querySelect('''
                SELECT * FROM "rol";
            ''')
    print(data)
    return render_template('rol/listadoRol.html', data=data)

#===========FIN ROL


@app.route('/altaUsuario')
def altaUsuario():
    #data = db.querySelect('''
    #           SELECT {} , {} FROM "combo";
     #       '''.format('"nombre"', '"total"'))
   # print(data)
    return render_template('rol/altaUsuario.html')    
    
#=========================Pruebas===================================



#Inicio de aplicacion
if __name__ == '__main__':
    app.run(debug=True)