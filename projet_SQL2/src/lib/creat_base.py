import mysql.connector,sqlite3
import lib.simple_fonction as X

class BDD():
    def __init__(self):
        #self.conn = sqlite3.connect('..//data//ma_base.db')
        self.conn = mysql.connector.connect(host='localhost',database='bdd2new',user='root',password='')
        self.cursor = self.conn.cursor()  
    def request_line(self,data):
        try:
            self.cursor.execute(data)
            try:
                msg = self.cursor.fetchall()
            except:
                msg = "INSERTION REUSSI"
            self.conn.commit()
        except Exception as e:
            msg = "@E :" + str(e)
        return msg
    
    def request(self,lst):
        res = []
        lst = X.parser(lst,';')
        for i in lst:
            res.append(self.request_line(i))
        return res
  
        