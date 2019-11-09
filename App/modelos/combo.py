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
    def alta_combo(self):
        pass

    def baja_combo(self):
        pass

    def modificar_combo(self):
        pass

    def consultar_combo(self):
        pass 