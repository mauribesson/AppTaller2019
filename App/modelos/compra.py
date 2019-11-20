from db import Database

db = Database()

#Modelo Compra 
class Compra:
    def __init__(self):
        self.__id = None
        self.__id_carrito = None
        self.__monto_compra = None
        self.__estado_confirmacion = None #Bool 

    #setter
    def set_id(self, pId):
        self.__id = pId

    def set_id_carrito(self, pIdCarrito):
        self.__id_carrito = pIdCarrito

    def set_monto_compra(self, pMontoCompra):
        self.__monto_compra = pMontoCompra

    def set_estado_confirmacion(self, pEstadpConfirmacion):
        self.__estado_confirmacion = pEstadpConfirmacion
    
    #getteres
    def get_id(self):
        return self.__id

    def get_id_carrito(self):
        return self.__id_carrito

    def get_monto_compra(self):
        return self.__monto_compra

    def get_estado_confirmacion(self):
        return self.__estado_confirmacion

    #logica 
    def alta_compra(self):
        data = db.queryInsert('''
            INSERT INTO "compra" ("idCarrito", "montoCompra", "estadoConfirmacion") 
            values ('{}', '{}','{}');
            '''.format(self.__id_carrito, self.__monto_compra, self.__estado_confirmacion)) 
        return data
        
    def baja_compra(self):
        data = db.queryInsert('''
               DELETE FROM "compra" WHERE "id" = '{}'; 
            '''.format(self.__id))
        return data
        
    def modificar_compra(self, pPuevoMontoCompra, pNuevoEstadoConfirmacion):       
        data = db.queryInsert('''
               UPDATE "compra"
	                SET "montoCompra" = '{}', 
                    "estadoConfirmacion" = '{}'
	                WHERE "id" = '{}';
            '''.format(pPuevoMontoCompra, 
                        pNuevoEstadoConfirmacion, 
                        self.__id))
        return data        
    
    def consultar_compra(self):
        data = db.querySelect('''
                SELECT * FROM "compra";
            ''')
        return data       