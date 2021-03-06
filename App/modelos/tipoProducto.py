from db import Database
 
db = Database()

#Modelo TipoProducto 
class TipoProducto:
    def __init__(self):
        self.__id = None
        self.__nombreTipo = ''

    #Setter
    def set_id(self, pId):
        self.__id = pId
    
    def set_nombre_tipo(self, pNombre):
        self.__nombreTipo = pNombre

    #Getter
    def get_id(self):
        return self.__id
    
    def get_nombre_tipo(self):
        return self.__nombreTipo

    #Logica
    def verificar_unico_tipo_producto(self):
        verificador = []
        verificador = db.querySelect('''
                SELECT * FROM "tipoProducto" WHERE "nombreTipo" = '{}';
            '''.format(self.__nombreTipo))
        return verificador

    def alta_tipo_producto(self):
        data = db.queryInsert('''
                 INSERT INTO "tipoProducto" ("nombreTipo") values ('{}');
                '''.format(self.__nombreTipo))
        return data

    def baja_tipo_producto(self):
        data = db.queryInsert('''
               DELETE FROM "tipoProducto" WHERE "idTipo" = {}; 
            '''.format(int(self.__id)))
        return data        

    def modificar_tipo_producto(self, pNuevoTipoNombre):
        data = db.queryInsert('''
               UPDATE "tipoProducto"
	                SET "nombreTipo" = '{}'
	                WHERE "nombreTipo" = '{}';
            '''.format(pNuevoTipoNombre, self.__nombreTipo))
        return data

    def consultar_tipo_producto(self):
            data = db.querySelect('''
                SELECT * FROM "tipoProducto";
            ''')
            return data

    def consultar_tipo_producto_por_id(self):
        id = str(self.__id)
        data = db.querySelect(
            '''
                SELECT * FROM "tipoProducto"
                WHERE "idTipo" = {};
            '''.format(id))
        return data[0]

    def formato_datos_tabla(self):
        ListaTipoProd = self.consultar_tipo_producto()
        nueva_lista = []

        for e in ListaTipoProd:
            nueva_lista.append({'id':e[0],  'tipo':e[1]})
        
        return nueva_lista
