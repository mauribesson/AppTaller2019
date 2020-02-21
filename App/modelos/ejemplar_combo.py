from db import Database
 
db = Database()

#Modelo Ejemplar_combo 
class Ejemplar_combo:
    def __init__(self):
        self.__idCombo = None
        self.__numeroSerie = None 

    #Setter
    def set_numero_serie(self, pNumeroSerie):
        self.__numeroSerie = pNumeroSerie
    
    def set_idCombo(self, pIdCombo):
        self.__idCombo = pIdCombo

    #Getter
    def get_numero_serie(self):
        return self.__numeroSerie
    
    def get_idCombo(self):
        return self.__idCombo

    #Logica        

    def alta_ejemplar_combo(self):
        data = db.queryInsert('''
                INSERT INTO "ejemplar_combo" 
                ("idCombo","numeroSerie") 
                values ('{}','{}');
                '''.format(
                    self.__idCombo,
                    self.__numeroSerie))
        return data

    def baja_ejemplar_combo(self):
        data = db.queryInsert('''
               DELETE FROM "ejemplar_combo" WHERE "numeroSerie" = '{}' AND "idCombo" = {}; 
            '''.format(
                self.__numeroSerie,
                self.__idCombo))
        return data

    def modificar_ejemplar_combo(self, pNuevoNumeroSerie):
        data = db.queryInsert('''
                    UPDATE "ejemplar_combo"
                            SET "numeroSerie" = '{}'
                            WHERE "numeroSerie" = '{}';
                    '''.format(
                        pNuevoNumeroSerie, 
                        self.__numeroSerie))
        return data

    def ejemplares_de_un_combo(self, id_Combo):
        data = db.querySelect('''
                SELECT * FROM "ejemplar_combo"
                WHERE "idCombo" = '{}';
            '''.format(id_Combo))
        return data

    def eliminar_ejemplares_combo(self):
        data = db.queryInsert('''
               DELETE FROM "ejemplar_combo" WHERE "idCombo" = {}; 
            '''.format(
                self.__idCombo))
        return data
