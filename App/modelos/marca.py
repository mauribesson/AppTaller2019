from db import Database
 
db = Database()

#Modelo Marca 
class Marca:
    def __init__(self):
        self.__id = None
        self.__nombre = ''

    #Setter
    def set_id(self, pId):
        self.__id = pId
    
    def set_nombre(self, pNombre):
        self.__nombre = pNombre

    #Getter
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre

    #Logica
    def alta_marca(self):
        pass

    def baja_marca(self):
        pass

    def modificar_marca(self):
        pass

    def consultar_marca(self):
        pass

