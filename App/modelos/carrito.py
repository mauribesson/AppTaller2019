from db import Database

db = Database()

#Modelo Carrito 
class Carrito:
    def __init__(self):
        self.__id= None
        self.__productos = []
        self.__total = None

    #setter
    def set_id(self, pId):
        self.__id = pId

    def set_productos(self, pProductos = []):
        self.__productos = pProductos

    def set_total(self, pTotal):
        self.__total = pTotal

    #getteres
    def get_id(self):
        return self.__id

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total

    #logica 
    def alta_carrito(self):
        pass

    def baja_carrito(self):
        pass

    def modificar_carrito(self):
        pass

    def consultar_carrito(self):
        pass
