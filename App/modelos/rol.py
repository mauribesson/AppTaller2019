from db import Database
 
db = Database() 

#Modelo Rol 
class Rol:
    def __init__(self):
        self.__id = None
        self.__nombreRol = ''

    #setter
    def set_id(self, pId):
        self.__id = pId
 
    def set_nombreRol(self, pNombreRol):
        self.__nombreRol = pNombreRol

    #getter
    def get_id(self):
        return self.__id 

    def get_nombreRol(self):
        return self.__nombreRol   

    #logica 
    def verificar_unico_rol(self):
        verificador = db.querySelect('''
            SELECT * FROM "rol" WHERE "nombreRol" = '{}';
         '''.format(self.__nombreRol))
        return verificador

    def alta_rol(self):
        data = []      
        data = db.queryInsert('''
                    INSERT INTO "rol" ("nombreRol") values ('{}');
                    '''.format(self.__nombreRol))
        return data       

    def baja_rol(self):
        data = db.queryInsert('''
               DELETE FROM "rol" WHERE "nombreRol" = '{}'; 
            '''.format(self.__nombreRol))
        return data

    def modificar_rol(self, pNuevoNombreRol):
        data = db.queryInsert('''
               UPDATE "rol"
	                SET "nombreRol" = '{}'
	                WHERE "nombreRol" = '{}';
            '''.format(pNuevoNombreRol, self.__nombreRol))
        return data

    def listar_rol(self):
        data = db.querySelect('''
                SELECT * FROM "rol";
            ''')
        return data

    def consultar_rol_por_id(self):
        id = str(self.__id)
        data = db.querySelect(
            '''
                SELECT * FROM "rol"
                WHERE "idRol" = {};
            '''.format(id))
        return data

    def formato_datos_tabla(self):
        ListaRoles = self.listar_rol()
        nueva_lista = []

        for e in ListaRoles:
            nueva_lista.append({'id':e[0], 'rol':e[1]})
        
        return nueva_lista
