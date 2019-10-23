import psycopg2

class Database: 
    def __init__(self):        
        pass

    def query(self, query=""):  
        self.connect = psycopg2.connect(host="localhost", 
                                        port="5432", 
                                        database="AppTaller2019", 
                                        user="postgres", 
                                        password="12345678"
                                        )        
        self.cursor = self.connect.cursor()    
        self.cursor.execute(query)
        #result = self.cursor.fetchone()
        result = self.cursor.fetchall()
        self.cursor.close()
        self.connect.close()
        return result