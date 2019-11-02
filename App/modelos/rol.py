from db import Database
 
db = Database() 

#Modelo Rol 
class Rol:
    def __init__(self):
        self._id = None
        self._nombreRol = ''

    def set_id(self, pId):
        self._id = pId

    def get_id(self):
        return self._id 

    def set_nombreRol(self, pNombreRol):
        self._nombreRol = pNombreRol

    def get_nombreRol(self):
        return self._nombreRol   

    def verificar_unico_rol(self, pNombreRol):
        verificador = db.querySelect('''
            SELECT * FROM "rol" WHERE "nombreRol" = '{}';
         '''.format(pNombreRol)) 
        return verificador

    def alta_rol(self, pNombreRol):
        data = []      
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
