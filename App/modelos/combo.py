from db import Database
 
db = Database()

#Modelo Combo 
class Combo:
    def __init__(self):
        self.__id = None
        self.__productos = []
        self.__nombre = ''
        self.__total = None
        self.__descuento = None

   #Setter
    def set_id(self, pId):
        self.__id = pId
    
    def set_productos(self, pProductos):
        self.__productos = pProductos

    def set_nombre(self, pNombre):
        self.__nombre = pNombre

    def set_total(self, pTotal):
        self.__total = pTotal

    def set_descuento(self, pDescuento):
        self.__descuento = pDescuento

    #Getter
    def get_id(self):
        return self.__id
    
    def get_productos(self):
        return self.__productos

    def get_nombre(self):
        return self.__nombre

    def get_total(self):
        return self.__total

    def get_descuento(self):
        return self.__descuento

    #Logica
    def verificar_combo(self):
        verificador = db.querySelect('''
                SELECT * FROM "combo" WHERE "nombre" = '{}';
            '''.format(self.__nombre))        
        return verificador

    def alta_combo(self):
        data = db.queryInsert('''
                INSERT INTO "combo" 
                ("nombre", "total", "descuento") 
                values ('{}','{}','{}');
                '''.format(self.__nombre, self.__total, self.__descuento))
        return data

    def baja_combo(self):
        data = db.queryInsert('''
               DELETE FROM "combo" WHERE "nombre" = '{}'; 
            '''.format(self.__nombre))
        return data

    def modificar_combo(self, pNuevoNombre, pNuevoTotal, pNuevoDescuento):
        data = db.queryInsert('''
               UPDATE "combo"
	                SET "nombre" = '{}', 
                    "total" = '{}', 
                    "descuento" = '{}'
	                WHERE "nombre" = '{}';
            '''.format(
                pNuevoNombre, 
                pNuevoTotal,
                pNuevoDescuento, 
                self.__nombre))
        return data

    def consultar_combo(self):
        data = db.querySelect('''
                SELECT * FROM "combo";
            ''') 
        return data