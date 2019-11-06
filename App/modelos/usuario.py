from db import Database
 
#Modelo Usuario 
class Usuario:
    def __init__(self):
        self._nombre = ""
        self._contrasenia = ""
        self._contacto = ""

    #setter
    def set_nombre(self, pNombre):
        self._nombre = pNombre

    def set_contrasenia(self, pPass):  
        self._contrasenia = pPass

    def set_contacto(self, pContacto):
        self._contacto = pContacto   

    #getter
    def get_nombre(self):
        return self._nombre

    def get_contrasenia(self):
        return self._contrasenia       

    def get_contacto(self):
        return self._contacto


    def alta_usuario(self):
        pass

    def baja_usuario(self):
        pass

    def modificar_usuario(self):
        pass

    def consultar_usuario(self):
        pass

    



