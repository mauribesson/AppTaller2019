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

    
    def obtener_ultimoscombosvendidos(self):
        data = db.querySelect(
                '''
                select * from "vista_combo_carrito" ORDER BY "idCarrito" DESC LIMIT 3
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