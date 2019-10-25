import psycopg2

class Database: 
    def __init__(self):  
        self.host = "localhost" 
        self.port = "5432" 
        self.database = "AppTaller2019" 
        self.user = "postgres" 
        self.password = "12345678"
        pass

    def query(self, query=""):  
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