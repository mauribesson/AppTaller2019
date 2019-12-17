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

    def modificar_usuario(self, pNuevaContrasenia, pNuevoContacto, nuevoRol):
        data = db.queryInsert('''
               UPDATE "usuario"
	                SET 
                    "contrasenia" = '{}', 
                    "contacto" = '{}',
                    "rol" = {}
	                WHERE "nombre" = '{}';
            '''.format( 
                        pNuevaContrasenia, 
                        pNuevoContacto, 
                        int(nuevoRol),
                        self.__nombre))
        return data

    def consultar_usuario(self):
        data = db.querySelect('''
                SELECT * FROM "vista_usuarios";
                ''')        
        return data

    def consultar_usuario_por_nombre(self):
            nombre = str(self.__nombre)
            data = db.querySelect(
                '''
                    SELECT * FROM "usuario"
                    WHERE "nombre" = '{}';
                '''.format(nombre))
            return data[0]#retorna la unica tupla 
        
    def formato_datos_tabla(self):
        ListaUsuarios = self.consultar_usuario()
        nueva_lista = []

        for e in ListaUsuarios:
            nueva_lista.append({'nombre':e[0],  'contacto':e[2], 'rol':e[3]})
        
        return nueva_lista

    



