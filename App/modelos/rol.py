from db import Database
 
db = Database() 

#Modelo Rol 
class Rol:
    def __init__(self):
        self.id = None
        self.nombreRol = ''


    def alta_rol(self, pNombreRol):
        data = []       
        verificador = db.querySelect('''
            SELECT * FROM "rol" WHERE "nombreRol" = '{}';
         '''.format(pNombreRol)) 
        if verificador == []:
            data = db.queryInsert('''
                    INSERT INTO "rol" ("nombreRol") values ('{}');
                    '''.format(pNombreRol))
        return data       

    def baja_rol(self):
        pass

    def modificar_rol(self):
        pass

    def consultar_rol(self):
        pass
