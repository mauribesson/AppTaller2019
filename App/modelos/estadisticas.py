from db import Database
 
db = Database()

#Modelo Usuario 
class Estadistica:

    def obtener_masvendidos(self):
        data = db.querySelect(
                '''
                SELECT DISTINCT "producto","nombre" 
                from "vista_ejemplar_carrito" 
                order by "producto" asc fetch first 3 rows only
                ''') 
        return data

    
    def obtener_combosmasvendidos(self):
        data = db.querySelect(
                '''
                SELECT DISTINCT "idCombo","nombre"
                from "vista_combo_carrito" 
                order by "nombre" asc fetch first 3 rows only
                ''') 
        return data

    def obtener_mejorescompradores(self):
        data = db.querySelect(
                '''
                SELECT DISTINCT "usuario"
                from "vista_compras" 
                order by "usuario" asc fetch first 3 rows only
                ''') 
        return data