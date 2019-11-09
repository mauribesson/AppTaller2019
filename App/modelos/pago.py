from db import Database
 
db = Database()

#Modelo Pago 
class Pago:
    def __init__(self):
        self.__total = None
        self.__estado = None #Booleano
        self.__tarjeta = None
        self.__cuotas = None                

   #Setter
    def set_total(self, pTotal):
        self.__total = pTotal

    def set_estado(self, pEstado):
        self.__estado = pEstado

    def set_tarjeta(self, pTarjeta):
        self.__tarjeta = pTarjeta
    
    def set_cuotas(self, pCuotas):
        self.__cuotas = pCuotas

    #Getter
    def get_total(self):
        return self.__total

    def get_estado(self):
        return self.__estado

    def get_tarjeta(self):
        return self.__tarjeta
    
    def get_cuotas(self):
        return self.__cuotas        

    #Logica
    def alta_pago(self):
        pass

    def baja_pago(self):
        pass

    def modificar_pago(self):
        pass

    def consultar_pago(self):
        pass 