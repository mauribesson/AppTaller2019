from db import Database
 
db = Database()

#Modelo Ejemplar 
class Ejemplar:
    def __init__(self):
        self.__numeroSerie = None
        self.__vendido = None #booleano
        self.__producto = None

    #Setter
    def set_numero_serie(self, pNumeroSerie):
        self.__numeroSerie = pNumeroSerie
    
    def set_vendido(self, pVendido):
        self.__vendido = pVendido

    def set_producto(self, pProducto):
        self.__producto = pProducto

    #Getter
    def get_numero_serie(self):
        return self.__numeroSerie
    
    def get_vendido(self):
        return self.__vendido

    def get_producto(self):
        return self.__producto

    #Logica
    def verificar_ejemplar(self):
        verificador = db.querySelect('''
                SELECT * FROM "ejemplar" WHERE "numeroSerie" = '{}';
            '''.format(self.__numeroSerie))
        return verificador        

    def alta_ejemplar(self):
        data = db.queryInsert('''
                INSERT INTO "ejemplar" 
                ("numeroSerie", "vendido", "producto") 
                values ('{}','{}','{}');
                '''.format(
                    self.__numeroSerie,
                    self.__vendido,
                    self.__producto))
        return data

    def baja_ejemplar(self):
        data = db.queryInsert('''
               DELETE FROM "ejemplar" WHERE "numeroSerie" = '{}'; 
            '''.format(self.__numeroSerie))
        return data

    def modificar_ejemplar(self, pNuevoNumeroSerie, pNuevoVendido, pNuevoProducto):
        data = db.queryInsert('''
                    UPDATE "ejemplar"
                            SET "numeroSerie" = '{}', 
                            "vendido" = '{}', 
                            "producto" = '{}'
                            WHERE "numeroSerie" = '{}';
                    '''.format(
                        pNuevoNumeroSerie,
                        pNuevoVendido, 
                        pNuevoProducto, 
                        self.__numeroSerie))
        return data

    def ejemplares_de_un_producto(self, producto):
        data = db.querySelect('''
                SELECT * FROM "ejemplar"
                WHERE "producto" = '{}';
            '''.format(producto))
        return data

    def ejemplares_de_un_producto_disponibles(self, producto):
        data = db.querySelect('''
                SELECT * FROM "ejemplar"
                WHERE "producto" = '{}' AND "vendido" = 'False';
            '''.format(producto))
        return data

    # Devuelve la cantidad disponible de ejemplares de un producto
    def cantidad_ejemplares_de_un_producto(self, producto):
        data = db.querySelect('''
                SELECT COUNT (*) FROM "ejemplar"
                WHERE "producto" = '{}' AND "vendido" = 'False';
            '''.format(producto))
        return data
        

    # Selecciona un ejemplar disponible para agregar al carrito
    def seleccionarEjemplares(self, producto):
        data = db.querySelect('''
                SELECT * FROM "ejemplar"
                WHERE "producto" = '{}' AND "vendido" = 'False';
            '''.format(producto))
        return data

    def consultar_ejemplar(self):
        data = db.querySelect('''
                SELECT * FROM "ejemplar";
            ''')
        return data

    def consultar_vista_ejemplares(self):
        data = db.querySelect(
            ''' 
            SELECT * FROM public.vista_ejemplares;
            ''')
        return data

    def precioDelEjemplar(self):
        data = db.querySelect('''
                SELECT * FROM "vista_ejemplar_combo" where "numeroSerie" = '{}';
                '''.format(
                    self.__numeroSerie))        
        return data

    def formato_datos_tabla(self):
        ListaEjemplar= self.consultar_vista_ejemplares()
        nueva_lista = []

        for e in ListaEjemplar:
            nueva_lista.append({'serie':e[0], 
                                'producto':e[2],
                                'vendido':e[1]})
        
        return nueva_lista

    def marcar_ejemplar_vendido(self, numeroSerie):
        data = db.queryInsert('''
                    UPDATE "ejemplar"
                            SET "vendido" = '{}'
                            WHERE "numeroSerie" = '{}';
                    '''.format(
                        True, 
                        numeroSerie))
        return data

    def marcar_ejemplar_disponible(self, numeroSerie):
        data = db.queryInsert('''
                    UPDATE "ejemplar"
                            SET "vendido" = '{}'
                            WHERE "numeroSerie" = '{}';
                    '''.format(
                        False, 
                        numeroSerie))
        return data

    def precio_ejemplar(self, numeroSerie):
        data = db.querySelect('''
                SELECT * FROM "vista_ejemplares" where "numeroSerie" = '{}';
                '''.format(numeroSerie))        
        return data