import psycopg2

class Database: 
    def __init__(self):  
        self.host = "localhost" 
        self.port = "5432" 
        self.database = "AppTaller2019" 
        self.user = "postgres" 
        self.password = "admin"  # Mauricio: 12345678 ; andrea: admin
        pass

    #para hacer querys tipo select que retornan 0 o mas elemntos
    def querySelect(self, query=""):  
        self.connect = psycopg2.connect(host=self.host, 
                                        port=self.port, 
                                        database=self.database, 
                                        user=self.user, 
                                        password=self.password
                                        )        
        self.cursor = self.connect.cursor()    
        self.cursor.execute(query)
        #result = self.cursor.fetchone()
        result = self.cursor.fetchall()        
        self.cursor.close()
        self.connect.close()
        return result

    #para hacer querys tipo insert update delete, consultas que retornan catidad de rows afectada.
    def queryInsert(self, query=""):  
        self.connect = psycopg2.connect(host=self.host, 
                                        port=self.port, 
                                        database=self.database, 
                                        user=self.user, 
                                        password=self.password
                                        )        
        self.cursor = self.connect.cursor()    
        self.cursor.execute(query)
        #result = self.cursor.fetchone()
        self.connect.commit()
        result = self.cursor.rowcount        
        self.cursor.close()
        self.connect.close()
        return result

    def manejar_error():
        pass    