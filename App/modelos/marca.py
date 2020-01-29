from db import Database
 
db = Database()

#Modelo Marca 
class Marca:
    def __init__(self):
        self.__id = None
        self.__nombre = ''

    #Setter
    def set_id(self, pId):
        self.__id = pId
    
    def set_nombre(self, pNombre):
        self.__nombre = pNombre

    #Getter
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre

    #Logica
    def verificar_unica_marca(self):
        verificador = db.querySelect('''
                SELECT * FROM "marca" WHERE "nombre" = '{}';
            '''.format(self.__nombre))
        return verificador

    def alta_marca(self):
        data = db.queryInsert('''
                INSERT INTO "marca" ("nombre") values ('{}');
                '''.format(self.__nombre)) 
        return data    

    def baja_marca(self):
        data = db.queryInsert('''
               DELETE FROM "marca" WHERE "idMarca" = {}; 
            '''.format(int(self.__id)))
        return data

    def modificar_marca(self, pNuevoNombre):
        data = db.queryInsert('''
               UPDATE "marca"
	                SET "nombre" = '{}'
	                WHERE "nombre" = '{}';
            '''.format(pNuevoNombre, self.__nombre))        
        return data

    def consultar_marca(self):
        data = db.querySelect('''
                SELECT * FROM "marca" WHERE "idMarca" = {}; 
            '''.format(int(self.__id)))
        return data[0]

    def listar_marca(self):
        data = db.querySelect('''
                SELECT * FROM "marca";
            ''')
        return data

    def formato_datos_tabla(self):
        ListaMarca= self.listar_marca()
        nueva_lista = []

        for e in ListaMarca:
            nueva_lista.append({'id':e[0],  'marca':e[1]})
        
        return nueva_lista
