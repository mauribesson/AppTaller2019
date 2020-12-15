from db import Database
 
db = Database()

#Modelo Combo 
class Combo:
    def __init__(self):
        self.__id = None
        self.__productos = []
        self.__nombre = ''
        self.__total = None
        self.__descuento = None
        self.__totalConDescuento = None
        self.__vendido = None

   #Setter
    def set_id(self, pId):
        self.__id = pId
    
    def set_productos(self, pProductos):
        self.__productos = pProductos

    def set_nombre(self, pNombre):
        self.__nombre = pNombre

    def set_total(self, pTotal):
        self.__total = pTotal

    def set_descuento(self, pDescuento):
        self.__descuento = pDescuento

    def set_totalConDescuento(self, ptotalConDescuento):
        self.__totalConDescuento = ptotalConDescuento

    def set_vendido(self, pVendido):
        self.__vendido = pVendido

    #Getter
    def get_id(self):
        return self.__id
    
    def get_productos(self):
        return self.__productos

    def get_nombre(self):
        return self.__nombre

    def get_total(self):
        return self.__total

    def get_descuento(self):
        return self.__descuento

    def get_totalConDescuento(self):
        return self.__totalConDescuento

    def get_vendido(self):
        return self.__vendido

    #Logica
    def verificar_combo(self):
        verificador = db.querySelect('''
                SELECT * FROM "combo" WHERE "nombre" = '{}';
            '''.format(self.__nombre))        
        return verificador

    def alta_combo(self):
        data = db.queryInsert('''
                INSERT INTO "combo" 
                ("nombre", "total", "descuento", "totalConDescuento", "vendido") 
                values ('{}', '{}', '{}', '{}', '{}');
                '''.format(self.__nombre, 0, 0, 0, False))
        return data

    def baja_combo(self):
        data = db.queryInsert('''
               DELETE FROM "combo" WHERE "id" = '{}'; 
            '''.format(self.__id))
        return data

    def modificar_combo(self, pNuevoNombre):
        data = db.queryInsert('''
               UPDATE "combo"
	                SET "nombre" = '{}'
	                WHERE "id" = '{}';
            '''.format(
                pNuevoNombre,  
                self.__id))
        return data

    def consultar_combo(self):
        data = db.querySelect('''
                SELECT * FROM "combo";
            ''') 
        return data

    def consultar_combo_por_id(self):
        data = db.querySelect('''
                SELECT * FROM "combo" WHERE "id" = '{}';
            '''.format(
                self.__id))
        return data

    def consultar_precio_combo(self):
        data = db.querySelect('''
                SELECT "total" FROM "combo" WHERE "id" = '{}';
            '''.format(
                self.__id))
        return data

    def listar_combos(self):
        data = db.querySelect('''
                SELECT * FROM "combo" where "vendido" = '{}';
            '''.format(False))
        return data

    def listar_poductos_del_combo(self, idCombo):
        data = db.querySelect('''
                SELECT * FROM "vista_ejemplar_combo" where "idCombo" = {};
                '''.format(
                    int(idCombo)))        
        return data

    def formato_datos_tabla_productos(self, idCombo):
        ListaCombos = self.listar_poductos_del_combo(idCombo)
        nueva_lista = []

        for e in ListaCombos:
            nueva_lista.append({'idCombo':e[0], 'numeroSerie':e[1], 'vendido':e[2], 'nombre':e[4], 'precio':e[5]})
        
        return nueva_lista

    def formato_datos_tabla(self):
        ListaCombos = self.listar_combos()
        nueva_lista = []

        for e in ListaCombos:
            nueva_lista.append({'id':e[0], 'nombre':e[1], 'total':e[2], 'descuento':e[3], 'totalConDescuento':e[4], 'vendido':e[5]})
        
        return nueva_lista
    
    def verCombo(self):
        data = db.querySelect('''
                SELECT * FROM "combo";
            ''') 
        return data

    def acumular_total(self, id, precio):
        data = db.queryInsert('''
               UPDATE "combo"
	                SET "total" = '{}'
	                WHERE "id" = '{}';
            '''.format(
                precio, 
                id))
        return data

    def cambiar_precio(self, id, nuevoTotal):
        data = db.queryInsert('''
               UPDATE "combo"
	                SET "total" = '{}'
	                WHERE "id" = '{}';
            '''.format(
                nuevoTotal, 
                id))
        return data

    def cambiar_total(self, nuevoTotal):
        data = db.queryInsert('''
               UPDATE "combo"
	                SET "total" = '{}'
	                WHERE "id" = '{}';
            '''.format(
                nuevoTotal, 
                self.__id))
        return data


    def aplicarDescuento(self, idCombo, totalConDesc,descuento):
        data = db.queryInsert('''
            UPDATE "combo"
                SET "totalConDescuento" = '{}',
                    "descuento" = '{}'
                WHERE "id" = '{}';
            '''.format(
                totalConDesc,
                descuento,
                idCombo))
        return data
    
    def consultar_descuento_combo(self):
        data = db.querySelect('''
                SELECT "descuento" FROM "combo" WHERE "id" = '{}';
            '''.format(
                self.__id))
        return data

    def total_combo_conDescuento(self, idCombo):
        data = db.querySelect('''
                SELECT "totalConDescuento" FROM "combo" WHERE "id" = '{}';
            '''.format(idCombo))
        return data

    def total_combo(self, idCombo):
        data = db.querySelect('''
                SELECT "total" FROM "combo" WHERE "id" = '{}';
            '''.format(idCombo))
        return data

    def id_combo(self, nombreCombo):
        data = db.querySelect('''
                SELECT "id" FROM "combo" WHERE "nombre" = '{}';
            '''.format(nombreCombo))
        return data

    def actualizarDescuento(self, totalConDesc):
        data = db.queryInsert('''
            UPDATE "combo"
                SET "totalConDescuento" = '{}'
                WHERE "id" = '{}';
            '''.format(
                totalConDesc,
                self.__id))
        return data

    def listar_combos_detallados(self):
        data = db.querySelect('''
            SELECT * FROM "vista_ejemplar_combo";
        '''.format(
            self.__id))
        return data


    def marcar_combo_vendido(self, id):
        data = db.queryInsert('''
                    UPDATE "combo"
                            SET "vendido" = '{}'
                            WHERE "id" = '{}';
                    '''.format(
                        True, 
                        id))
        return data

    def marcar_combo_disponible(self, id):
        data = db.queryInsert('''
                    UPDATE "combo"
                            SET "vendido" = '{}'
                            WHERE "id" = '{}';
                    '''.format(
                        False, 
                        id))
        return data

    