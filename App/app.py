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

#========ABM usuario
@app.route('/altaUsuario')
def altaUsuario():
     return render_template('usuario/altaUsuario.html') 

@app.route('/guardarUsuario', methods=["POST"])
def guardarUsuario():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombreUsuario']
        contrasenia = request.form['contrasenia']
        contacto = request.form['contacto']
        verificador = db.querySelect('''
                SELECT * FROM "usuario" WHERE "nombre" = '{}';
            '''.format(nombre))
        
        if verificador == []:
            data = db.queryInsert('''
                INSERT INTO "usuario" ("nombre", "contrasenia", "contacto", "rol") values ('{}', '{}', '{}', 1);
                '''.format(nombre, contrasenia, contacto))    
    return render_template('usuario/usuarioGuardado.html', data=data, verificador=verificador)  

@app.route('/bajaUsuario') 
def bajaUsuario():
    return render_template('usuario/bajaUsuario.html')  

@app.route('/eliminarUsuario', methods=["POST"])
def eliminarUsuario():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        data = db.queryInsert('''
               DELETE FROM "usuario" WHERE "nombre" = '{}'; 
            '''.format(nombre))

    return render_template('usuario/usuarioEliminado.html', data=data)    

@app.route('/modificarUsuario') 
def modificarUsuario():
    return render_template('usuario/modificarUsuario.html')  

@app.route('/editarUsuario', methods=["POST"])
def editarUsuario():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        nombreNuevo = request.form['nombreNuevo']
        contraseniaNueva = request.form['contraseniaNueva']
        contactoNuevo = request.form['contactoNuevo']  
        data = db.queryInsert('''
               UPDATE "usuario"
	                SET "nombre" = '{}', "contrasenia" = '{}', "contacto" = '{}'
	                WHERE "nombre" = '{}';
            '''.format(nombreNuevo, contraseniaNueva, contactoNuevo, nombre))

    return render_template('usuario/usuarioModificado.html', data=data)

@app.route('/listarUsuario')
def listarUsuario():
    data = db.querySelect('''
                SELECT * FROM "usuario";
            ''')
    return render_template('usuario/listadoUsuario.html', data=data)   
    



#========ABM tipoProducto
@app.route('/altaTipoProducto')
def altaTipoProducto():
     return render_template('tipoProducto/altaTipoProducto.html') 

@app.route('/guardarTipoProducto', methods=["POST"])
def guardarTipoProducto():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        data = db.queryInsert('''
               INSERT INTO "tipoProducto" ("nombreTipo") values ('{}');
            '''.format(nombre))
   
    return render_template('tipoProducto/tipoProductoGuardado.html', data=data)  

@app.route('/bajaTipoProducto') 
def bajaTipoProducto():
    return render_template('tipoProducto/bajaTipoProducto.html')  

@app.route('/eliminarTipoProducto', methods=["POST"])
def eliminarTipoProducto():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        data = db.queryInsert('''
               DELETE FROM "tipoProducto" WHERE "nombreTipo" = '{}'; 
            '''.format(nombre))

    return render_template('tipoProducto/tipoProductoEliminado.html', data=data)    

@app.route('/modificarTipoProducto') 
def modificarTipoProducto():
    return render_template('tipoProducto/modificarTipoProducto.html')  

@app.route('/editarTipoProducto', methods=["POST"])
def editarTipoProducto():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        nombreNuevo = request.form['nombreNuevo']
        data = db.queryInsert('''
               UPDATE "tipoProducto"
	                SET "nombreTipo" = '{}'
	                WHERE "nombreTipo" = '{}';
            '''.format(nombreNuevo, nombre))

    return render_template('tipoProducto/tipoProductoModificado.html', data=data)

@app.route('/listarTipoProducto')
def listarTipoProducto():
    data = db.querySelect('''
                SELECT * FROM "tipoProducto";
            ''')
    return render_template('tipoProducto/listadoTipoProducto.html', data=data)


#====MARCA
@app.route('/altaMarca')
def altaMarca():
     return render_template('marca/altaMarca.html') 

@app.route('/guardarMarca', methods=["POST"])
def guardarMarca():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        data = db.queryInsert('''
               INSERT INTO "marca" ("nombre") values ('{}');
            '''.format(nombre))
   
    return render_template('marca/marcaGuardada.html', data=data)  

@app.route('/bajaMarca') 
def bajaMarca():
    return render_template('marca/bajaMarca.html')  

@app.route('/eliminarMarca', methods=["POST"])
def eliminarMarca():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        data = db.queryInsert('''
               DELETE FROM "marca" WHERE "nombre" = '{}'; 
            '''.format(nombre))

    return render_template('marca/marcaEliminada.html', data=data)    

@app.route('/modificarMarca') 
def modificarMarca():
    return render_template('marca/modificarMarca.html')  

@app.route('/editarMarca', methods=["POST"])
def editarMarca():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        nombreNuevo = request.form['nombreNuevo']
        data = db.queryInsert('''
               UPDATE "marca"
	                SET "nombre" = '{}'
	                WHERE "nombre" = '{}';
            '''.format(nombreNuevo, nombre))

    return render_template('marca/marcaModificada.html', data=data)

@app.route('/listarMarca')
def listarMarca():
    data = []
    data = db.querySelect('''
                SELECT * FROM "marca";
            ''')
    return render_template('marca/listadoMarca.html', data=data)


#====PRODUCTO
@app.route('/altaProducto')
def altaProducto():
     return render_template('producto/altaProducto.html') 

@app.route('/guardarProducto', methods=["POST"])
def guardarProducto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion'] 
        precio = request.form['precio']
        modelo = request.form['modelo']
        garantia = request.form['garantia']
        tipoProducto = request.form['tipoProducto']
        marca = request.form['marca'] 
        data = db.queryInsert('''
               INSERT INTO "producto" 
               ("nombre", "descripcion", "precio", "modelo", "garantia", "tipoProducto", "marca") 
               values ('{}','{}','{}','{}','{}','{}','{}');
            '''.format(nombre, descripcion, precio, modelo, garantia, tipoProducto, marca))
   
    return render_template('producto/productoGuardado.html', data=data)  

@app.route('/bajaProducto') 
def bajaProducto():
    return render_template('producto/bajaProducto.html')  

@app.route('/eliminarProducto', methods=["POST"])
def eliminarProducto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        data = db.queryInsert('''
               DELETE FROM "producto" WHERE "nombre" = '{}'; 
            '''.format(nombre))

    return render_template('producto/productoEliminado.html', data=data)    

@app.route('/modificarProducto') 
def modificarProducto():
    return render_template('producto/modificarProducto.html')  

@app.route('/editarProducto', methods=["POST"])
def editarProducto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevoNombre = request.form['nuevoNombre']
        nuevaDescripcion = request.form['nuevaDescripcion']
        nuevoPrecio = request.form['nuevoPrecio']
        nuevoModelo = request.form['nuevoModelo']
        nuevaGarantia = request.form['nuevaGarantia']
        nuevoTipoProducto = request.form['nuevoTipoProducto']
        nuevaMarca = request.form['nuevaMarca']
        data = db.queryInsert('''
               UPDATE "producto"
	                SET "nombre" = '{}', 
                    "descripcion" = '{}', 
                    "precio" = '{}', 
                    "modelo" = '{}', 
                    "garantia" = '{}', 
                    "tipoProducto" = '{}', 
                    "marca" = '{}'
	                WHERE "nombre" = '{}';
            '''.format(nuevoNombre, nuevaDescripcion, nuevoPrecio, nuevoModelo, nuevaGarantia, nuevoTipoProducto, nuevaMarca, nombre))

    return render_template('producto/productoModificado.html', data=data)

@app.route('/listarProducto')
def listarProducto():
    data = db.querySelect('''
                SELECT * FROM "producto";
            ''')
    return render_template('producto/listadoProducto.html', data=data)


#=========================Pruebas===================================



#Inicio de aplicacion
if __name__ == '__main__':
    app.run(debug=True)