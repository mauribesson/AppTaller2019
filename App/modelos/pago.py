from db import Database
 
db = Database()

#Modelo Pago 
class Pago:
    def __init__(self):
        self.__id = None
        self.__id_compra = None
        self.__total = None
        self.__estado = None #Booleano
        self.__tarjeta = None
        self.__cuotas = None                

   #Setter
    def set_id(self, pId):
        self.__id = pId

    def set_id_compra(self, pIdCompra):
        self.__id_compra = pIdCompra

    def set_total(self, pTotal):
        self.__total = pTotal

    def set_estado(self, pEstado):
        self.__estado = pEstado

    def set_tarjeta(self, pTarjeta):
        self.__tarjeta = pTarjeta
    
    def set_cuotas(self, pCuotas):
        self.__cuotas = pCuotas

    #Getter
    def get_id(self):
        return self.__id

    def get_id_compra(self):
        return self.__id_compra

    def get_total(self):
        return self.__total

    def get_estado(self):
        return self.__estado

    def get_tarjeta(self):
        return self.__tarjeta
    
    def get_cuotas(self):
        return self.__cuotas        

    #Logica
    def alta_pago(self):
        data = db.queryInsert('''
            INSERT INTO "pago" ("idCompra", "total", "estado", "tarjeta", "cuotas") 
            values ('{}', '{}', '{}', '{}', '{}');
            '''.format(
             self.__id_compra,
             self.__total,
             self.__estado,
             self.__tarjeta,
             self.__cuotas)) 
        return data

    def baja_pago(self):
        data = db.queryInsert('''
               DELETE FROM "pago" WHERE "id" = '{}'; 
            '''.format(self.__id))
        return data    

    def modificar_pago(self, pNuevoTotal, pNuevoEstado, pNuevaTarjeta, pNuevoCuotas):
        data = db.queryInsert('''
               UPDATE "pago"
	                SET "total" = {},
                     "estado" = '{}',
                      "tarjeta" = '{}',
                       "cuotas" = {}
	                WHERE "id" = '{}';
            '''.format(
                pNuevoTotal,
                pNuevoEstado,
                pNuevaTarjeta,
                pNuevoCuotas, 
                self.__id))
        return data

    def consultar_pago(self):
        data = db.querySelect('''
                SELECT * FROM "pago";
            ''')  
        return data