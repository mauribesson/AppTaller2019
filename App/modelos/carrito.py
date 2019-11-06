from db import Database
 
#Modelo Carrito 
class Carrito:
    def __init__(self):
        self._id= None
        self._productos = []
        self._total = None

    #setter
    def set_id(self, pId):
        self._id = pId

    def set_productos(self, pProductos = []):
        self._productos = pProductos

    def set_total(self, pTotal):
        self._total = pTotal

    #getteres
    def get_id(self):
        return self._id

    def get_productos(self):
        return self._productos

    def get_total(self):
        return self._total

    #logica 
    def alta_carrito(self):
        pass

    def baja_carrito(self):
        pass

    def modificar_carrito(self):
        pass

    def consultar_carrito(self):
        pass
