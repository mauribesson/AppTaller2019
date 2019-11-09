from db import Database
 
db = Database()

#Modelo Ejemplar 
class Ejemplar:
    def __init__(self):
        self.__numeroSerie = None
        self.__vendido = None #booleano

    #Setter
    def set_numero_serie(self, pNumeroSerie):
        self.__numeroSerie = pNumeroSerie
    
    def set_vendido(self, pVendido):
        self.__vendido = pVendido

    #Getter
    def get_numero_serie(self):
        return self.__numeroSerie
    
    def get_vendido(self):
        return self.__vendido

    #Logica
    def alta_ejemplar(self):
        pass

    def baja_ejemplar(self):
        pass

    def modificar_ejemplar(self):
        pass

    def consultar_ejemplar(self):
        pass