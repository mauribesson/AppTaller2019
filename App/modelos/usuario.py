from db import Database
 
db = Database()

#Modelo Usuario 
class Usuario:
    def __init__(self):
        self.__nombre = ""
        self.__contrasenia = ""
        self.__contacto = ""

    #setter
    def set_nombre(self, pNombre):
        self.__nombre = pNombre

    def set_contrasenia(self, pPass):  
        self.__contrasenia = pPass

    def set_contacto(self, pContacto):
        self.__contacto = pContacto   

    #getter
    def get_nombre(self):
        return self.__nombre

    def get_contrasenia(self):
        return self.__contrasenia       

    def get_contacto(self):
        return self.__contacto


    def alta_usuario(self):
        pass

    def baja_usuario(self):
        pass

    def modificar_usuario(self):
        pass

    def consultar_usuario(self):
        pass

    



