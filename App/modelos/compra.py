from db import Database

db = Database()

#Modelo Compra 
class Compra:
    def __init__(self):
        self.__id = None
        self.__id_carrito = None
        self.__monto_compra = None
        self.__fecha = None
        self.__estado_confirmacion = None #Bool 

    #setter
    def set_id(self, pId):
        self.__id = pId

    def set_id_carrito(self, pIdCarrito):
        self.__id_carrito = pIdCarrito

    def set_monto_compra(self, pMontoCompra):
        self.__monto_compra = pMontoCompra

    def set_fecha(self, pFecha):
        self.__fecha = pFecha

    def set_estado_confirmacion(self, pEstadpConfirmacion):
        self.__estado_confirmacion = pEstadpConfirmacion
    
    #getteres
    def get_id(self):
        return self.__id

    def get_id_carrito(self):
        return self.__id_carrito

    def get_monto_compra(self):
        return self.__monto_compra

    def get_fecha(self):
        return self.__fecha

    def get_estado_confirmacion(self):
        return self.__estado_confirmacion

    #logica 
    def alta_compra(self):
        data = db.queryInsert('''
            INSERT INTO "compra" ("idCarrito", "montoCompra", "estadoConfirmacion", "fecha") 
            values ('{}', '{}','{}', '{}');
            '''.format(self.__id_carrito, self.__monto_compra, self.__estado_confirmacion, self.__fecha)) 
        return data
        
    def baja_compra(self, idCompra):
        data = db.queryInsert('''
               DELETE FROM "compra" WHERE "id" = {}; 
            '''.format(idCompra))
        return data

    def mis_compras(self, usuario):
        data = db.querySelect('''
                SELECT * FROM "compra_pago" WHERE "usuario" = '{}';
            '''.format(usuario))
        return data 

    def id_compra(self, id_carrito):
        data = db.querySelect('''
                SELECT "id" FROM "compra" WHERE "idCarrito" = '{}';
            '''.format(id_carrito))
        return data  

    def compra_pendiente_pago(self, pUsuario):
            data = db.querySelect('''
                    SELECT * FROM "vista_compras" 
                    WHERE "usuario" = '{}' AND "estadoConfirmacion" = 'False';
            '''.format(pUsuario))
            return data

    def compra_confirmada(self, idCompra):
        data = db.queryInsert('''
                UPDATE "compra"
                    SET "estadoConfirmacion" = '{}'
                    WHERE "id" = '{}';
            '''.format(True, idCompra))
        return data

    def ventas(self):
        data = db.querySelect('''
                SELECT * FROM "vista_compras";
            ''')
        return data 


    def ejemplares_venta(self, idCompra):
        data = db.querySelect('''
                select * from "vista_ejemplar_compra" where "id" = '{}';
            '''.format(idCompra))
        return data 

    def ventas_por_fecha(self, fechaDesde, fechaHasta):
        data = db.querySelect('''
                select * from "vista_compras" where "fecha" between '{}' and '{}';
            '''.format(fechaDesde, fechaHasta))
        return data 

    # No se usaría    
    """ def modificar_compra(self, pPuevoMontoCompra, pNuevoEstadoConfirmacion):       
        data = db.queryInsert('''
               UPDATE "compra"
	                SET "montoCompra" = '{}', 
                    "estadoConfirmacion" = '{}'
	                WHERE "id" = '{}';
            '''.format(pPuevoMontoCompra, 
                        pNuevoEstadoConfirmacion, 
                        self.__id))
        return data  """       
    
          