from db import Database

db = Database()

#Modelo Producto 
class Producto:
    def __init__(self):
        self.__id = None
        self.__nombre = ''
        self.__descripcion = ''
        self.__precio = None
        self.__modelo = None
        self.__garantia = None
        self.__tipo_producto = None
        self.__marca = None

    #Setter
    def set_id(self, pId):
        self.__id = pId
    
    def set_nombre(self, pNombre):
        self.__nombre = pNombre
    
    def set_descripcion(self, pDescripcio):
        self.__descripcion = pDescripcio

    def set_precio(self, pPrecio):
        self.__precio = pPrecio

    def set_modelo(self, pModelo):
        self.__modelo = pModelo   

    def set_garantia(self, pGarantia):
        self.__garantia = pGarantia

    def set_tipo_producto(self, pTipoProducto):
        self.__tipo_producto = pTipoProducto

    def set_marca(self, pMarca):
        self.__marca = pMarca

    #Getter
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_descripcion(self):
        return self.__descripcion

    def get_precio(self):
        return self.__precio

    def get_modelo(self):
        return self.__modelo   

    def get_garantia(self):
        return self.__garantia
    
    def get_tipo_producto(self):
        return self.__tipo_producto

    def get_marca(self):
        return self.__marca

    #Logica
    def verificar_unico_producto(self):
        verificador = db.querySelect('''
                SELECT * FROM "producto" WHERE "nombre" = '{}';
            '''.format(self.__nombre))
        return verificador

    def alta_producto(self):
        data =[]
        data = db.queryInsert('''
             INSERT INTO "producto" 
                ("nombre", "descripcion", "precio", "modelo", "garantia", "tipoProducto", "marca") 
                values ('{}','{}','{}','{}','{}','{}','{}');
                '''.format(
                        self.__nombre, 
                        self.__descripcion, 
                        self.__precio, 
                        self.__modelo, 
                        self.__garantia, 
                        self.__tipo_producto, 
                        self.__marca))
        return data

    def baja_producto(self):
        data = db.queryInsert('''
               DELETE FROM "producto" WHERE "id" = {}; 
            '''.format(int(self.__id)))
        return data


    def modificar_producto(self, pNuevoNombre, pNuevaDescripcion, pNuevoPrecio, pNuevoModelo, pNuevaGarantia, pNuevoTipoProducto, pNuevaMarca):
        data = db.queryInsert('''
                                UPDATE "producto"
                                        SET "nombre" = '{}', 
                                        "descripcion" = '{}', 
                                        "precio" = '{}', 
                                        "modelo" = '{}', 
                                        "garantia" = '{}', 
                                        "tipoProducto" = '{}', 
                                        "marca" = '{}'
                                        WHERE "id" = {};
                                '''.format(
                                        pNuevoNombre,
                                        pNuevaDescripcion,
                                        pNuevoPrecio,
                                        pNuevoModelo,
                                        pNuevaGarantia,
                                        pNuevoTipoProducto,
                                        pNuevaMarca,
                                        int(self.__id)))
        return data

    def consultar_producto(self):
        data =[]
        data = db.querySelect('''
                SELECT * FROM "producto";
            ''')
        return data 

    def stock(self):         
        stock = None
        #Agregar logica de stock aca
        return stock

    def consultar_vista_productos(self):
        data = db.querySelect(
            ''' 
            SELECT * FROM public.vista_productos;
            ''')
        return data  

    def listar_productos(self):
        data = db.querySelect('''
                SELECT * FROM "vista_productos";
            ''')
        return data 
    
    def obtener_precio(self, id):
        data = db.querySelect('''
            SELECT "precio" FROM "producto" WHERE "id" = '{}';
        '''.format(id))
        return data

    def formato_datos_tabla(self):
        ListaMarca= self.listar_productos()
        nueva_lista = []

        for e in ListaMarca:
            nueva_lista.append({'id': e[0],
                                'nombre':e[1],
                                'descripcion': e[2],
                                'precio': e[3],
                                'modelo':e[4],
                                'garantia':e[5],
                                'marca': e[6],
                                'tipoProducto':e[7]
                                })
        
        return nueva_lista

    def consultar_producto_por_id(self):
        data = db.querySelect('''
            SELECT * FROM "vista_productos" WHERE "id" = {};
        '''.format(int(self.__id)))
        return data[0]

    def obtener_cantidad_productos(self):
        data =[]
        data = db.querySelect('''
                SELECT count(*) FROM producto;;
            ''')
        return data

    def consultar_producto_por_tipo(self, tipoProducto):
        data = db.querySelect('''
            SELECT * FROM "vista_productos" WHERE "tipoProducto" = '{}';
        '''.format(tipoProducto))
        return data

    def consultar_producto_por_marca(self, marca):
        data = db.querySelect('''
            SELECT * FROM "vista_productos" WHERE "marca" = '{}';
        '''.format(marca))
        return data