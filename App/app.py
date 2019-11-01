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
    data = []
    if request.method == 'POST':
        nombre = request.form['nombreRol']
        verificador = db.querySelect('''
                SELECT * FROM "rol" WHERE "nombreRol" = '{}';
            '''.format(nombre)) 
        if verificador == []:
            data = db.queryInsert('''
                INSERT INTO "rol" ("nombreRol") values ('{}');
                '''.format(nombre))
   
    return render_template('rol/rolGuardado.html', data=data, verificador=verificador)  

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
        verificador = db.querySelect('''
                SELECT * FROM "tipoProducto" WHERE "nombreTipo" = '{}';
            '''.format(nombre)) 
        if verificador == []:
            data = db.queryInsert('''
                 INSERT INTO "tipoProducto" ("nombreTipo") values ('{}');
                '''.format(nombre))
   
    return render_template('tipoProducto/tipoProductoGuardado.html', data=data, verificador=verificador)  

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
        verificador = db.querySelect('''
                SELECT * FROM "marca" WHERE "nombre" = '{}';
            '''.format(nombre)) 
        if verificador == []:
            data = db.queryInsert('''
                INSERT INTO "marca" ("nombre") values ('{}');
                '''.format(nombre))
   
    return render_template('marca/marcaGuardada.html', data=data, verificador=verificador)  

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
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion'] 
        precio = request.form['precio']
        modelo = request.form['modelo']
        garantia = request.form['garantia']
        tipoProducto = request.form['tipoProducto']
        marca = request.form['marca'] 
        verificador = db.querySelect('''
                SELECT * FROM "producto" WHERE "nombre" = '{}';
            '''.format(nombre)) 
        if verificador == []:
            data = db.queryInsert('''
                INSERT INTO "producto" 
                ("nombre", "descripcion", "precio", "modelo", "garantia", "tipoProducto", "marca") 
                values ('{}','{}','{}','{}','{}','{}','{}');
                '''.format(nombre, descripcion, precio, modelo, garantia, tipoProducto, marca))
   
    return render_template('producto/productoGuardado.html', data=data, verificador=verificador)  

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


#====EJEMPLAR
@app.route('/altaEjemplar')
def altaEjemplar():
     return render_template('ejemplar/altaEjemplar.html') 

@app.route('/guardarEjemplar', methods=["POST"])
def guardarEjemplar():
    data = []
    if request.method == 'POST':
        numeroSerie = request.form['numeroSerie']
        vendido = request.form['vendido'] 
        producto = request.form['producto']
        verificador = db.querySelect('''
                SELECT * FROM "ejemplar" WHERE "numeroSerie" = '{}';
            '''.format(numeroSerie)) 
        if verificador == []:
            data = db.queryInsert('''
                INSERT INTO "ejemplar" 
                ("numeroSerie", "vendido", "producto") 
                values ('{}','{}','{}');
                '''.format(numeroSerie, vendido, producto))
   
    return render_template('ejemplar/ejemplarGuardado.html', data=data, verificador=verificador)  

@app.route('/bajaEjemplar') 
def bajaEjemplar():
    return render_template('ejemplar/bajaEjemplar.html')  

@app.route('/eliminarEjemplar', methods=["POST"])
def eliminarEjemplar():
    if request.method == 'POST':
        numeroSerie = request.form['numeroSerie']
        data = db.queryInsert('''
               DELETE FROM "ejemplar" WHERE "numeroSerie" = '{}'; 
            '''.format(numeroSerie))

    return render_template('ejemplar/ejemplarEliminado.html', data=data)    

@app.route('/modificarEjemplar') 
def modificarEjemplar():
    return render_template('ejemplar/modificarEjemplar.html')  

@app.route('/editarEjemplar', methods=["POST"])
def editarEjemplar():
    if request.method == 'POST':
        numeroSerie = request.form['numeroSerie']
        nuevoNumeroSerie = request.form['nuevoNumeroSerie']
        nuevoVendido = request.form['nuevoVendido']
        nuevoProducto = request.form['nuevoProducto']
        data = db.queryInsert('''
               UPDATE "ejemplar"
	                SET "numeroSerie" = '{}', 
                    "vendido" = '{}', 
                    "producto" = '{}'
	                WHERE "numeroSerie" = '{}';
            '''.format(nuevoNumeroSerie, nuevoVendido, nuevoProducto, numeroSerie))

    return render_template('ejemplar/ejemplarModificado.html', data=data)

@app.route('/listarEjemplar')
def listarEjemplar():
    data = db.querySelect('''
                SELECT * FROM "ejemplar";
            ''')
    return render_template('ejemplar/listadoEjemplar.html', data=data)


#====COMMBO
@app.route('/altaCombo')
def altaCombo():
     return render_template('combo/altaCombo.html') 

@app.route('/guardarCombo', methods=["POST"])
def guardarCombo():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio'] 
        descuento = request.form['descuento']
        verificador = db.querySelect('''
                SELECT * FROM "combo" WHERE "nombre" = '{}';
            '''.format(nombre)) 
        if verificador == []:
            data = db.queryInsert('''
                INSERT INTO "combo" 
                ("nombre", "precio", "precio") 
                values ('{}','{}','{}');
                '''.format(nombre, precio, descuento))
   
    return render_template('combo/comboGuardado.html', data=data, verificador=verificador)  

@app.route('/bajaCombo') 
def bajaCombo():
    return render_template('combo/bajaCombo.html')  

@app.route('/eliminarCombo', methods=["POST"])
def eliminarCombo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        data = db.queryInsert('''
               DELETE FROM "combo" WHERE "nombre" = '{}'; 
            '''.format(nombre))

    return render_template('combo/comboEliminado.html', data=data)    

@app.route('/modificarCombo') 
def modificarCombo():
    return render_template('combo/modificarCombo.html')  

@app.route('/editarCombo', methods=["POST"])
def editarCombo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevoNombre = request.form['nuevoNombre']
        nuevoPrecio = request.form['nuevoPrecio']
        nuevoDescuento = request.form['nuevoDescuento']
        data = db.queryInsert('''
               UPDATE "combo"
	                SET "nombre" = '{}', 
                    "precio" = '{}', 
                    "descuento" = '{}'
	                WHERE "nombre" = '{}';
            '''.format(nuevoNombre, nuevaPrecio, nuevoDescuento, nombre))

    return render_template('combo/comboModificado.html', data=data)

@app.route('/listarCombo')
def listarCombo():
    data = db.querySelect('''
                SELECT * FROM "combo";
            ''')
    return render_template('combo/listadoCombo.html', data=data)


#======== ejemplar_combo
@app.route('/altaEjemplar_combo')
def altaEjemplar_combo():
     return render_template('ejemplar_combo/altaEjemplar_combo.html') 

@app.route('/guardarEjemplar_combo', methods=["POST"])
def guardarEjemplar_combo():
    data = []
    if request.method == 'POST':
        idCombo = request.form['idCombo']
        numeroSerie = request.form['numeroSerie']
        data = db.queryInsert('''
            INSERT INTO "ejemplar_combo" ("idCombo", "numeroSerie") values ('{}', '{}');
            '''.format(idCombo, numeroSerie))    

@app.route('/bajaEjemplar_combo') 
def bajaEjemplar_combo():
    return render_template('ejemplar_combo/bajaEjemplar_combo.html')  

@app.route('/eliminarEjemplar_combo', methods=["POST"])
def eliminarEjemplar_combo():
    data = []
    if request.method == 'POST':
        idCombo = request.form['idCombo']
        numeroSerie = request.form['numeroSerie']
        data = db.queryInsert('''
               DELETE FROM "ejemplar_combo" WHERE "idCombo" = '{}' AND "numeroSerie" = '{}'; 
            '''.format(idCombo, numeroSerie))   

@app.route('/modificarEjemplar_combo') 
def modificarEjemplar_combo():
    return render_template('ejemplar_combo/modificarEjemplar_combo.html')  

@app.route('/editarEjemplar_combo', methods=["POST"])
def editarEjemplar_combo():
    data = []
    if request.method == 'POST':
        idCombo = request.form['idCombo']
        numeroSerie = request.form['numeroSerie']
        nuevoIdCombo = request.form['nuevoIdCombo']
        nuevoNumeroSerie = request.form['nuevoNumeroSerie']  
        data = db.queryInsert('''
               UPDATE "ejemplar_combo"
	                SET "idCombo" = '{}', "numeroSerie" = '{}'
	                WHERE "idCombo" = '{}' AND "numeroSerie" = '{}';
            '''.format(nuevoIdCombo, nuevoNumeroSerie, idCombo, numeroSerie))

@app.route('/listarEjemplar_combo')
def listarEjemplar_combo():
    data = db.querySelect('''
                SELECT * FROM "ejemplar_combo";
            ''')
    return render_template('ejemplar_combo/listadoEjemplar_combo.html', data=data)   
    


#====CARRITO
@app.route('/altaCarrito')
def altaCarrito():
     return render_template('carrito/altaCarrito.html') 

@app.route('/guardarCarrito', methods=["POST"])
def guardarCarrito():
    data = []
    if request.method == 'POST':
        total = request.form['total']
        data = db.queryInsert('''
            INSERT INTO "carrito" ("total") values ('{}');
            '''.format(total)) 

@app.route('/bajaCarrito') 
def bajaCarrito():
    return render_template('carrito/bajaCarrito.html')  

@app.route('/eliminarCarrito', methods=["POST"])
def eliminarCarrito():
    if request.method == 'POST':
        id = request.form['id']
        data = db.queryInsert('''
               DELETE FROM "carrito" WHERE "id" = '{}'; 
            '''.format(id))

    return render_template('carrito/carritoEliminado.html', data=data)    

@app.route('/modificarCarrito') 
def modificarCarrito():
    return render_template('carrito/modificarCarrito.html')  

@app.route('/editarCarrito', methods=["POST"])
def editarCarrito():
    if request.method == 'POST':
        total = request.form['total']
        id = request.form['id']
        data = db.queryInsert('''
               UPDATE "carrito"
	                SET "total" = '{}'
	                WHERE "id" = '{}';
            '''.format(total, id))

    return render_template('carrito/carritoModificado.html', data=data)

@app.route('/mostrarCarrito')
def mostrarCarrito():
    data = db.querySelect('''
                SELECT * FROM "carrito";
            ''')
    return render_template('carrito/mostrarCarrito.html', data=data)



#=========================Pruebas===================================



#Inicio de aplicacion
if __name__ == '__main__':
    app.run(debug=True)