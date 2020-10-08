import mercadopago
import json

from db import Database
 
db = Database()

#Modelo MercadoPago 
class MercadoPago:
    def __init__(self):
        self.__id = None
        self.__id_compra = None
        self.__total = None
        self.__link_pago = None
        self.__estado = None #Booleano                

   #Setter
    def set_id(self, pId):
        self.__id = pId

    def set_id_compra(self, pIdCompra):
        self.__id_compra = pIdCompra

    def set_total(self, pTotal):
        self.__total = pTotal

    def set_link_pago(self, pLink_pago):
        self.__link_pago = pLink_pago

    def set_estado(self, pEstado):
        self.__estado = pEstado

    #Getter
    def get_id(self):
        return self.__id

    def get_id_compra(self):
        return self.__id_compra

    def get_total(self):
        return self.__total

    def get_linkPago(self):
        return self.__link_pago

    def get_estado(self):
        return self.__estado        

    #Logica
    def alta_mercadopago(self):
        data = db.queryInsert('''
            INSERT INTO "mercadopago" ("id", "idCompra", "total", "link_pago", "estado") 
            values ('{}', '{}', '{}', '{}', '{}');
            '''.format(
             self.__id,
             self.__id_compra,
             self.__total,
             self.__link_pago,
             self.__estado)) 
        return data

    def baja_mercadopago(self):
        data = db.queryInsert('''
               DELETE FROM "mercadopago" WHERE "id" = '{}'; 
            '''.format(self.__id))
        return data    

    def consultar_mercadopago(self):
        data = db.querySelect('''
                SELECT * FROM "mercadopago" WHERE "id" = '{}'; 
            '''.format(self.__id))
        return data

    def link_mercadopago(self, idCompra):
        data = db.querySelect('''
                SELECT "link_pago" FROM "mercadopago" WHERE "idCompra" = '{}';
            '''.format(idCompra))
        return data


def nuevaReerencia_mercadoPago(idPago, total):
    mp = mercadopago.MP(4907324296549149, "hUM1unn6xSSpvIZkOVgkE6Yr3JG2t6b7")
    preference = {
        "items": [
            {
                "title": idPago,
                "quantity": 1,
                "currency_id": "ARS",
                "unit_price": total
            }
        ]
    }
    preferenceResult = mp.create_preference(preference)
    return preferenceResult,

def consultarReferencia_mercadoPago(id):
    mp = mercadopago.MP(4907324296549149, "hUM1unn6xSSpvIZkOVgkE6Yr3JG2t6b7")
    preferenceResult = mp.get_preference(id)
    return preferenceResult

## NO FUNCIONA, VER QUE ID SE DEBE PASAR
## Cancelar pago, solo para pagos pendientes
def cancelar_cupon(id):
    mp = mercadopago.MP(4907324296549149, "hUM1unn6xSSpvIZkOVgkE6Yr3JG2t6b7")
    result = mp.cancel_payment(id)
    return json.dumps(result, indent=4)