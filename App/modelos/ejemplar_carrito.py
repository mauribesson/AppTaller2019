from db import Database
 
db = Database()

#Modelo Ejemplar_carrito 
class Ejemplar_carrito:
    def __init__(self):
        self.__idCarrito = None
        self.__numeroSerie = None 

    #Setter
    def set_numero_serie(self, pNumeroSerie):
        self.__numeroSerie = pNumeroSerie
    
    def set_idCarrito(self, pIdCarrito):
        self.__idCarrito = pIdCarrito

    #Getter
    def get_numero_serie(self):
        return self.__numeroSerie
    
    def get_idCarrito(self):
        return self.__idCarrito

    #Logica        

    def alta_ejemplar_carrito(self):
        data = db.queryInsert('''
                INSERT INTO "ejemplar_carrito" 
                ("idCarrito","numeroSerie") 
                values ('{}','{}');
                '''.format(
                    self.__idCarrito,
                    self.__numeroSerie))
        return data

    def baja_ejemplar_carrito(self):
        data = db.queryInsert('''
               DELETE FROM "ejemplar_carrito" WHERE "numeroSerie" = '{}' AND "idCarrito" = {}; 
            '''.format(
                self.__numeroSerie,
                self.__idCarrito))
        return data

    def ejemplares_de_un_carrito(self, id_carrito):
        data = db.querySelect('''
                SELECT * FROM "vista_ejemplar_carrito"
                WHERE "idCarrito" = '{}';
            '''.format(id_carrito))
        return data


