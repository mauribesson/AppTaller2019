from flask import Flask, render_template, request
from db import Database
from modelos.rol import Rol
from modelos.usuario import Usuario
from modelos.tipoProducto import TipoProducto
from modelos.marca import Marca
from modelos.producto import Producto
from modelos.ejemplar import Ejemplar
from modelos.combo import Combo

db = Database()

app = Flask(__name__)

@app.route('/')
def index():
    data = []
    return render_template('index.html', data=data)

""" @app.route('/altausuario')
def altausuario():
    data = []
    return render_template('index.html', data=data)
 """
#Seleccionar todos los combos 
""" @app.route('/pruebaCombo')
def pruebaCombo():
    data = db.querySelect('''
                SELECT {} , {} FROM "combo";
            '''.format('"nombre"', '"total"'))
    print(data)
    return render_template('index.html', data=data) """


#=========================ABMS===================================
#====ROL
#Alta Rol 
@app.route('/altaRol')
def altaRol():
     return render_template('rol/altaRol.html') 

@app.route('/guardarRol', methods=["POST"])
def guardarRol():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombreRol']
        rol =  Rol()
        rol.set_nombreRol(nombre)
        verificador = rol.verificar_unico_rol()
        if verificador == []:
            data = rol.alta_rol()   
    return render_template('rol/rolGuardado.html', data=data, verificador=verificador)  
#Fin Alta Rol

#Baja Rol
@app.route('/bajaRol') 
def bajaRol():
    return render_template('rol/bajaRol.html')  

@app.route('/eliminarRol', methods=["POST"])
def eliminarRol():
    if request.method == 'POST':
        nombre = request.form['nombreRol']
        rol =  Rol()
        rol.set_nombreRol(nombre)
        data = rol.baja_rol()
    return render_template('rol/rolEliminado.html', data=data)    
#Fin Baja Rol

#Modificar Rol
@app.route('/modificarRol') 
def modificarRol():
    return render_template('rol/modificarRol.html')  

@app.route('/editarRol', methods=["POST"])
def editarRol():
    if request.method == 'POST':
        nombre = request.form['nombreRol']
        nombreNuevo = request.form['nombreNuevoRol']
        rol = Rol()
        rol.set_nombreRol(nombre)
        data = rol.modificar_rol(nombreNuevo)     
    return render_template('rol/rolModificado.html', data=data)

# Listar Rol
@app.route('/listarRol')
def listarRol():
    rol = Rol()
    data = rol.listar_rol()
    return render_template('rol/listadoRol.html', data=data)
# Fin Listar Rol

@app.route('/verRol/<int:id>')
def verRol(id):
    rol = Rol()
    rol.set_id(id)
    data = rol.consultar_rol_por_id()
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

        usuario = Usuario()
        usuario.set_nombre(nombre)
        usuario.set_contrasenia(contrasenia)
        usuario.set_contacto(contacto)

        verificador = usuario.verificar_unico_usuario()  

        if verificador == []:
            data = usuario.alta_usuario() 
    return render_template('usuario/usuarioGuardado.html', data=data, verificador=verificador)  

@app.route('/bajaUsuario') 
def bajaUsuario():
    return render_template('usuario/bajaUsuario.html')  

@app.route('/eliminarUsuario', methods=["POST"])
def eliminarUsuario():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        usuario = Usuario()
        usuario.set_nombre(nombre)
        data = usuario.baja_usuario()
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

        usuario = Usuario()
        usuario.set_nombre(nombre)
        usuario.modificar_usuario(nombreNuevo, contraseniaNueva, contactoNuevo)
    return render_template('usuario/usuarioModificado.html', data=data)

@app.route('/listarUsuario')
def listarUsuario():
    data = []
    usuario = Usuario()
    data = usuario.consultar_usuario() 
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
        tipo_producto = TipoProducto()
        tipo_producto.set_nombre_tipo(nombre)
        verificador = tipo_producto.verificar_unico_tipo_producto()

        if verificador == []: 
            data = tipo_producto.alta_tipo_producto()     
    return render_template('tipoProducto/tipoProductoGuardado.html', data=data, verificador=verificador)  

@app.route('/bajaTipoProducto') 
def bajaTipoProducto():
    return render_template('tipoProducto/bajaTipoProducto.html')  

@app.route('/eliminarTipoProducto', methods=["POST"])
def eliminarTipoProducto():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']

        tipo_producto = TipoProducto()
        tipo_producto.set_nombre_tipo(nombre)
        data = tipo_producto.baja_tipo_producto()

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
        tipo_producto = TipoProducto()
        tipo_producto.set_nombre_tipo(nombre)
        data = tipo_producto.modificar_tipo_producto(nombreNuevo)

    return render_template('tipoProducto/tipoProductoModificado.html', data=data)

@app.route('/listarTipoProducto')
def listarTipoProducto():
    tipo_producto = TipoProducto()
    data = tipo_producto.consultar_tipo_producto()
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

        marca = Marca()
        marca.set_nombre(nombre)
        verificador = marca.verificar_unica_marca() 

        if verificador == []:
            data = marca.alta_marca()   
    return render_template('marca/marcaGuardada.html', data=data, verificador=verificador)  

@app.route('/bajaMarca') 
def bajaMarca():
    return render_template('marca/bajaMarca.html')  

@app.route('/eliminarMarca', methods=["POST"])
def eliminarMarca():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = Marca()
        marca.set_nombre(nombre)
        data = marca.baja_marca()

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

        marca = Marca()
        marca.set_nombre(nombre)
        data = marca.modificar_marca(nombreNuevo)
    return render_template('marca/marcaModificada.html', data=data)

@app.route('/listarMarca')
def listarMarca():
    data = []
    marca = Marca()
    data = marca.consultar_marca()
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
        tipo_producto = request.form['tipoProducto']
        marca = request.form['marca'] 

        producto = Producto()
        producto.set_nombre(nombre)
        producto.set_descripcion(descripcion)
        producto.set_precio(precio)
        producto.set_modelo(modelo)
        producto.set_garantia(garantia)
        producto.set_tipo_producto(tipo_producto)
        producto.set_marca(marca)

        verificador = producto.verificar_unico_producto()
 
        if verificador == []:
            data = producto.alta_producto()          
    return render_template('producto/productoGuardado.html', data=data, verificador=verificador)  

@app.route('/bajaProducto') 
def bajaProducto():
    return render_template('producto/bajaProducto.html')  

@app.route('/eliminarProducto', methods=["POST"])
def eliminarProducto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        producto = Producto()
        producto.set_nombre(nombre)   
        data = producto.baja_producto()  
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
        
        producto = Producto()
        producto.set_nombre(nombre)  
        data = producto.modificar_producto(nuevoNombre, 
                                            nuevaDescripcion,
                                            nuevoPrecio,
                                            nuevoModelo,
                                            nuevaGarantia,
                                            nuevoTipoProducto,
                                            nuevaMarca)     
    return render_template('producto/productoModificado.html', data=data)

@app.route('/listarProducto')
def listarProducto():
    data = []
    producto = Producto()
    data = producto.consultar_producto() 
    return render_template('producto/listadoProducto.html', data=data)


#====EJEMPLAR
@app.route('/altaEjemplar')
def altaEjemplar():
     return render_template('ejemplar/altaEjemplar.html') 

@app.route('/guardarEjemplar', methods=["POST"])
def guardarEjemplar():
    data, verificador = [], []

    if request.method == 'POST':
        numeroSerie = request.form['numeroSerie']
        vendido = request.form['vendido'] 
        producto = request.form['producto']

        ejemplar = Ejemplar()
        ejemplar.set_numero_serie(numeroSerie)
        ejemplar.set_vendido(vendido)
        ejemplar.set_producto(producto)
        
        verificador = ejemplar.verificar_ejemplar()
 
        if verificador == []:
            data = ejemplar.alta_ejemplar()            
    return render_template('ejemplar/ejemplarGuardado.html', data=data, verificador=verificador)  

@app.route('/bajaEjemplar') 
def bajaEjemplar():
    return render_template('ejemplar/bajaEjemplar.html')  

@app.route('/eliminarEjemplar', methods=["POST"])
def eliminarEjemplar():
    if request.method == 'POST':
        numeroSerie = request.form['numeroSerie']
        ejemplar = Ejemplar()
        ejemplar.set_numero_serie(numeroSerie)
        data = ejemplar.baja_ejemplar()
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
        
        ejemplar = Ejemplar()
        ejemplar.set_numero_serie(numeroSerie)
        data = ejemplar.modificar_ejemplar(nuevoNumeroSerie, nuevoVendido, nuevoProducto )

    return render_template('ejemplar/ejemplarModificado.html', data=data)

@app.route('/listarEjemplar')
def listarEjemplar():
    data = []
    ejemplar = Ejemplar()
    data = ejemplar.consultar_ejemplar()
    return render_template('ejemplar/listadoEjemplar.html', data=data)

#====COMBO
@app.route('/altaCombo')
def altaCombo():
     return render_template('combo/altaCombo.html') 

@app.route('/guardarCombo', methods=["POST"])
def guardarCombo():
    data, verificador = [], []
    if request.method == 'POST':
        nombre = request.form['nombre']
        total = request.form['precioTotal'] 
        descuento = request.form['descuento']

        combo = Combo()
        combo.set_nombre(nombre)
        combo.set_total(total)
        combo.set_descuento(descuento)

        verificador = combo.verificar_combo() 
        if verificador == []:
            data = combo.alta_combo()   
    return render_template('combo/comboGuardado.html', data=data, verificador=verificador)  

@app.route('/bajaCombo') 
def bajaCombo():
    return render_template('combo/bajaCombo.html')  

@app.route('/eliminarCombo', methods=["POST"])
def eliminarCombo():
    if request.method == 'POST':
        nombre = request.form['nombre']

        combo = Combo()
        combo.set_nombre(nombre)

        data = combo.baja_combo()
    return render_template('combo/comboEliminado.html', data=data)    

@app.route('/modificarCombo') 
def modificarCombo():
    return render_template('combo/modificarCombo.html')  

@app.route('/editarCombo', methods=["POST"])
def editarCombo():
    data = []
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevoNombre = request.form['nuevoNombre']
        nuevoPrecioTotal = request.form['nuevoPrecio']
        nuevoDescuento = request.form['nuevoDescuento']
        
        combo = Combo()
        combo.set_nombre(nombre)

        data = combo.modificar_combo(nuevoNombre, nuevoPrecioTotal, nuevoDescuento)
    return render_template('combo/comboModificado.html', data=data)

@app.route('/listarCombo')
def listarCombo():
    combo = Combo()
    data = combo.consultar_combo()
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
    return render_template('index.html')   

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
    return render_template('index.html')

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
    return render_template('index.html')

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
    return render_template('index.html')
    
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
        total = request.form['nuevoTotal']
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


#======== ejemplar_carrito
@app.route('/altaEjemplar_carrito')
def altaEjemplar_carrito():
     return render_template('ejemplar_carrito/altaEjemplar_carrito.html') 

@app.route('/guardarEjemplar_carrito', methods=["POST"])
def guardarEjemplar_carrito():
    data = []
    if request.method == 'POST':
        idCarrito= request.form['idCarrito']
        numeroSerie = request.form['numeroSerie']
        data = db.queryInsert('''
            INSERT INTO "ejemplar_carrito" ("idCarrito", "numeroSerie") values ('{}', '{}');
            '''.format(idCarrito, numeroSerie))  
    return render_template('index.html')

@app.route('/bajaEjemplar_carrito') 
def bajaEjemplar_carrito():
    return render_template('ejemplar_carrito/bajaEjemplar_carrito.html')  

@app.route('/eliminarEjemplar_carrito', methods=["POST"])
def eliminarEjemplar_carrito():
    data = []
    if request.method == 'POST':
        idCarrito = request.form['idCarrito']
        numeroSerie = request.form['numeroSerie']
        data = db.queryInsert('''
               DELETE FROM "ejemplar_carrito" WHERE "idCarrito" = '{}' AND "numeroSerie" = '{}'; 
            '''.format(idCarrito, numeroSerie))   
    return render_template('index.html')

@app.route('/modificarEjemplar_carrito') 
def modificarEjemplar_carrito():
    return render_template('ejemplar_carrito/modificarEjemplar_carrito.html')  

@app.route('/editarEjemplar_carrito', methods=["POST"])
def editarEjemplar_carrito():
    data = []
    if request.method == 'POST':
        idCarrito = request.form['idCarrito']
        numeroSerie = request.form['numeroSerie']
        nuevoIdCarrito = request.form['nuevoIdCarrito']
        nuevoNumeroSerie = request.form['nuevoNumeroSerie']  
        data = db.queryInsert('''
               UPDATE "ejemplar_carrito"
	                SET "idCarrito" = '{}', "numeroSerie" = '{}'
	                WHERE "idCarrito" = '{}' AND "numeroSerie" = '{}';
            '''.format(nuevoIdCarrito, nuevoNumeroSerie, idCarrito, numeroSerie))
    return render_template('index.html')

@app.route('/listarEjemplar_carrito')
def listarEjemplar_carrito():
    data = db.querySelect('''
                SELECT * FROM "ejemplar_carrito";
            ''')
    return render_template('ejemplar_carrito/listadoEjemplar_carrito.html', data=data)   


#====COMPRA
@app.route('/altaCompra')
def altaCompra():
     return render_template('compra/altaCompra.html') 

@app.route('/guardarCompra', methods=["POST"])
def guardarCompra():
    data = []
    if request.method == 'POST':
        idCarrito = request.form['idCarrito']
        montoCompra = request.form['montoCompra']
        estadoConfirmacion = request.form['estadoConfirmacion']
        data = db.queryInsert('''
            INSERT INTO "compra" ("idCarrito", "montoCompra", "estadoConfirmacion") 
            values ('{}', '{}','{}');
            '''.format(idCarrito, montoCompra, estadoConfirmacion)) 
    return render_template('index.html')

@app.route('/bajaCompra') 
def bajaCompra():
    return render_template('compra/bajaCompra.html')  

@app.route('/eliminarCompra', methods=["POST"])
def eliminarCompra():
    if request.method == 'POST':
        id = request.form['id']
        data = db.queryInsert('''
               DELETE FROM "compra" WHERE "id" = '{}'; 
            '''.format(id))

    return render_template('compra/compraEliminada.html', data=data)    

@app.route('/modificarCompra') 
def modificarCompra():
    return render_template('compra/modificarCompra.html')  

@app.route('/editarCompra', methods=["POST"])
def editarCompra():
    if request.method == 'POST':
        id = request.form['id']
        nuevoMontoCompra = request.form['nuevoMontoCompra']
        nuevoEstadoConfirmacion = request.form['nuevoEstadoConfirmacion']
        data = db.queryInsert('''
               UPDATE "compra"
	                SET "montoCompra" = '{}', "estadoConfirmacion" = '{}'
	                WHERE "id" = '{}';
            '''.format(nuevoMontoCompra, nuevoEstadoConfirmacion, id))

    return render_template('compra/compraModificada.html', data=data)

@app.route('/mostrarCompra')
def mostrarCompra():
    data = db.querySelect('''
                SELECT * FROM "compra";
            ''')
    return render_template('compra/mostrarCompra.html', data=data)


#====PAGO
@app.route('/altaPago')
def altaPago():
     return render_template('pago/altaPago.html') 

@app.route('/guardarPago', methods=["POST"])
def guardarPago():
    data = []
    if request.method == 'POST':
        idCompra = request.form['idCompra']
        total = request.form['total']
        estado = request.form['estado']
        tarjeta = request.form['tarjeta']
        cuotas = request.form['cuotas']
        data = db.queryInsert('''
            INSERT INTO "pago" ("idCompra", "total", "estado", "tarjeta", "cuotas") 
            values ('{}', '{}', '{}', '{}', '{}');
            '''.format(idCompra, total, estado, tarjeta, cuotas)) 
    return render_template('index.html')

@app.route('/bajaPago') 
def bajaPago():
    return render_template('pago/bajaPago.html')  

@app.route('/eliminarPago', methods=["POST"])
def eliminarPago():
    if request.method == 'POST':
        id = request.form['id']
        data = db.queryInsert('''
               DELETE FROM "pago" WHERE "id" = '{}'; 
            '''.format(id))

    return render_template('pago/pagoEliminado.html', data=data)    

@app.route('/modificarPago') 
def modificarPago():
    return render_template('pago/modificarPago.html')  

@app.route('/editarPago', methods=["POST"])
def editarPago():
    if request.method == 'POST':
        id = request.form['id']
        nuevoTotal = request.form['nuevoTotal']
        nuevoEstado = request.form['nuevoEstado']
        nuevaTarjeta = request.form['nuevaTarjeta']
        nuevoCuotas = request.form['nuevoCuotas']
        data = db.queryInsert('''
               UPDATE "pago"
	                SET "total" = {}, "estado" = '{}', "tarjeta" = '{}', "cuotas" = {}
	                WHERE "id" = '{}';
            '''.format(nuevoTotal, nuevoEstado, nuevaTarjeta, nuevoCuotas, id))

    return render_template('pago/pagoModificado.html', data=data)

@app.route('/mostrarPago')
def mostrarPago():
    data = db.querySelect('''
                SELECT * FROM "pago";
            ''')
    return render_template('pago/mostrarPago.html', data=data)

    
#=========================Fin ABM===================================



#Inicio de aplicacion
if __name__ == '__main__':
    app.run(debug=True)