from db import Database
 
db = Database() 

#Modelo Rol 
class Rol:
    def __init__(self):
        self._id = None
        self._nombreRol = ''

    #setter
    def set_id(self, pId):
        self._id = pId
 
    def set_nombreRol(self, pNombreRol):
        self._nombreRol = pNombreRol
        
    #getter
    def get_id(self):
        return self._id 

    def get_nombreRol(self):
        return self._nombreRol   

    #logica 
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

    def baja_rol(self, pNombreRol):
        data = db.queryInsert('''
               DELETE FROM "rol" WHERE "nombreRol" = '{}'; 
            '''.format(pNombreRol))
        return data

    def modificar_rol(self, pNombreRol, pNuevoNombreRol):
        data = db.queryInsert('''
               UPDATE "rol"
	                SET "nombreRol" = '{}'
	                WHERE "nombreRol" = '{}';
            '''.format(pNuevoNombreRol, pNombreRol))
        return data

    def listar_rol(self):
        data = db.querySelect('''
                SELECT * FROM "rol";
            ''')
        return data

    def consultar_rol_por_id(self, pId):
        id = str(pId)
        data = db.querySelect(
            '''
                SELECT * FROM "rol"
                WHERE "idRol" = {};
            '''.format(id))
        return data
       
