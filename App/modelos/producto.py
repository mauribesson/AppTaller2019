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

    #Logica
    def alta_producto(self):
        pass

    def baja_producto(self):
        pass

    def modificar_producto(self):
        pass

    def consultar_producto(self):
        pass

    def stock(self):         
        stock = None
        #Agregar logica de stock aca
        return stock