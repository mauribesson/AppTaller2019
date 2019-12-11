from db import Database
 
db = Database()

#Modelo Usuario 
class Usuario:
    def __init__(self):
        self.__nombre = ""
        self.__contrasenia = ""
        self.__contacto = ""

    #setter
    def set_nombre(self, pNombre):
        self.__nombre = pNombre

    def set_contrasenia(self, pPass):  
        self.__contrasenia = pPass

    def set_contacto(self, pContacto):
        self.__contacto = pContacto   

    #getter
    def get_nombre(self):
        return self.__nombre

    def get_contrasenia(self):
        return self.__contrasenia       

    def get_contacto(self):
        return self.__contacto
    
    #Logica
    def verificar_unico_usuario(self):
        verificador = db.querySelect('''
                SELECT * FROM "usuario" WHERE "nombre" = '{}';
            '''.format(self.__nombre)) 
        return verificador  
        
    def alta_usuario(self):
        data = db.queryInsert(
                '''
                INSERT INTO "usuario" ("nombre",
                 "contrasenia",
                 "contacto",
                  "rol") 
                values ('{}', '{}', '{}', 1);
                '''.format(self.__nombre, self.__contrasenia,self.__contacto)) 
        return data

    def baja_usuario(self):
        data = db.queryInsert('''
               DELETE FROM "usuario" WHERE "nombre" = '{}'; 
            '''.format(self.__nombre))
        return data    

    def modificar_usuario(self, pNuevoNombre, pNuevaContrasenia, pNuevoContacto):
        data = db.queryInsert('''
               UPDATE "usuario"
	                SET "nombre" = '{}', 
                    "contrasenia" = '{}', 
                    "contacto" = '{}'
	                WHERE "nombre" = '{}';
            '''.format(pNuevoNombre, 
                        pNuevaContrasenia, 
                        pNuevoContacto, 
                        self.__nombre))
        return data

    def consultar_usuario(self):
        data = db.querySelect('''
                SELECT * FROM "usuario";
                ''')        
        return data

    """ 
    def consultar_rol_por_id(self):
            id = str(self.__id)
            data = db.querySelect(
                '''
                    SELECT * FROM "rol"
                    WHERE "idRol" = {};
                '''.format(id))
            return data
        """
    def formato_datos_tabla(self):
        ListaRoles = self.consultar_usuario()
        nueva_lista = []

        for e in ListaRoles:
            nueva_lista.append({'id':e[0], 'rol':e[1]})
        
        return nueva_lista

    



