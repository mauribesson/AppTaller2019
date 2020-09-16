from db import Database

db = Database()

#Modelo Imagenes
class Imagenes:
    def __init__(self):
        self.__id = None
        self.__idProducto = None
        self.__urlImagen = ''

    #Setter
    def set_id(self, pId):
        self.__id = pId
    
    def set_idProducto(self, pIdProducto):
        self.__idProducto = pIdProducto
    
    def set_urlImagen(self, pUrlImagen):
        self.__urlImagen = pUrlImagen

    #Getter
    def get_id(self):
        return self.__id
    
    def get_idProducto(self):
        return self.__idProducto
    
    def get_urlImagen(self):
        return self.__urlImagen



    #Logica

    # Cheque que si nombre de la imagen ya existe
    def verificar_unica_imagen(self):
        verificador = db.querySelect('''
                SELECT * FROM "imagenes" WHERE "urlImagen" = '{}';
            '''.format(self.__urlImagen))
        return verificador

    def alta_imagen(self):
        data =[]
        data = db.queryInsert('''
             INSERT INTO "imagenes" 
                ("idProducto", "urlImagen") 
                values ('{}','{}');
                '''.format(
                        self.__idProducto, 
                        self.__urlImagen))
        return data

    def baja_imagen(self):
        data = db.queryInsert('''
               DELETE FROM "imagenes" WHERE "id" = {}; 
            '''.format(int(self.__id)))
        return data

    def imagenes_producto(self, id):
        data = db.querySelect('''
            SELECT "urlImagen" FROM "imagenes" WHERE "idProducto" = '{}';
        '''.format(id))
        return data

    def obtener_cantidad_imagenes(self,id):
        data =[]
        data = db.querySelect('''
                SELECT count(*) FROM "imagenes" WHERE "idProducto" = '{}';
            '''.format(id))
        return data
