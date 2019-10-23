from db import Database
db = Database()

def pruebaCombo():

    id = input('idCombo:')
    data = db.query('''
                SELECT {} , {} FROM "combo" WHERE id = {};
            '''.format('"nombre"', '"total"', id))
    print(data)


pruebaCombo()

input('una tecla')



