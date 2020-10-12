from db import Database
 
db = Database()

#Modelo Ejemplar_carrito 
class Combo_carrito:
    def __init__(self):
        self.__idCarrito = None
        self.__idCombo = None 

    #Setter
    def set_idCombo(self, pIdCombo):
        self.__idCombo = pIdCombo
    
    def set_idCarrito(self, pIdCarrito):
        self.__idCarrito = pIdCarrito

    #Getter
    def get_idCombo(self):
        return self.__idCombo
    
    def get_idCarrito(self):
        return self.__idCarrito

    #Logica        

    def alta_combo_carrito(self):
        data = db.queryInsert('''
                INSERT INTO "combo_carrito" 
                ("idCarrito","idCombo") 
                values ('{}','{}');
                '''.format(
                    self.__idCarrito,
                    self.__idCombo))
        return data

    def baja_combo_carrito(self):
        data = db.queryInsert('''
               DELETE FROM "combo_carrito" WHERE "idCombo" = '{}' AND "idCarrito" = {}; 
            '''.format(
                self.__idCombo,
                self.__idCarrito))
        return data

    def combos_de_un_carrito(self, id_carrito):
        data = db.querySelect('''
                SELECT * FROM "vista_combo_carrito"
                WHERE "idCarrito" = '{}';
            '''.format(id_carrito))
        return data


