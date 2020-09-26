from db import Database

db = Database()

#Modelo Carrito 
class Carrito:
    def __init__(self):
        self.__id= None
        self.__productos = []
        self.__total = None
        self.__usuario = None
        self.__finalizado = False

    #setter
    def set_id(self, pId):
        self.__id = pId

    def set_productos(self, pProductos = []):
        self.__productos = pProductos

    def set_total(self, pTotal):
        self.__total = pTotal

    def set_usuario(self, pUsuario):
        self.__usuario = pUsuario

    def set_finalizado(self, pFinalizado):
        self.__finalizado = pFinalizado

    #getteres
    def get_id(self):
        return self.__id

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total

    def get_usuario(self):
        return self.__usuario

    def get_finalizado(self):
        return self.__finalizado

    #logica 
    def alta_carrito(self):
        data = db.queryInsert('''
            INSERT INTO "carrito" 
            ("total", "usuario", "finalizado") 
            values ('{}','{}','{}');
            '''.format(
                0,
                self.__usuario,
                False))
        return data 

    def baja_carrito(self):
        data = db.queryInsert('''
               DELETE FROM "carrito" WHERE "id" = '{}'; 
            '''.format(self.__id)) 
        return data   

    
    def consultar_carrito(self):
        data = db.querySelect('''
                SELECT * FROM "carrito";
            ''')
        return data

    def carrito_actual(self, pUsuario):
        data = db.querySelect('''
                SELECT * FROM "carrito" 
                WHERE "usuario" = '{}' AND "finalizado" = 'False';
        '''.format(pUsuario))
        return data


    def actualizar_total_carrito(self, pTotal, idCarrito):
        data = db.queryInsert('''
               UPDATE "carrito"
	                SET "total" = '{}'
	                WHERE "id" = '{}';
            '''.format(pTotal, idCarrito))
        return data

    def carrito_finalizado(self, idCarrito):
        data = db.queryInsert('''
                UPDATE "carrito"
                    SET "finalizado" = '{}'
                    WHERE "id" = '{}';
            '''.format(True, idCarrito))
        return data

    def carrito_activo(self, idCarrito):
        data = db.queryInsert('''
                UPDATE "carrito"
                    SET "finalizado" = '{}'
                    WHERE "id" = '{}';
            '''.format(False, idCarrito))
        return data