from db import Database
 
db = Database()

#Modelo TipoProducto 
class TipoProducto:
    def __init__(self):
        self.__id = None
        self.__nombreTipo = ''

    #Setter
    def set_id(self, pId):
        self.__id = pId
    
    def set_nombre_tipo(self, pNombre):
        self.__nombreTipo = pNombre

    #Getter
    def get_id(self):
        return self.__id
    
    def get_nombre_tipo(self):
        return self.__nombreTipo

    #Logica
    def alta_tipo_producto(self):
        pass

    def baja_tipo_producto(self):
        pass

    def modificar_tipo_producto(self):
        pass

    def consultar_tipo_producto(self):
        pass

