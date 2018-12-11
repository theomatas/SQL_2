import mysql.connector,sqlite3
import lib.simple_fonction as X

class BDD():
    def __init__(self):
        #self.conn = sqlite3.connect('..//data//ma_base.db')
        self.conn = mysql.connector.connect(host='localhost',database='SQL2',user='root',password='')
        self.cursor = self.conn.cursor()  
    def request_line(self,data):
        try:
            self.cursor.execute(data)
            msg = self.cursor.fetchall()
            self.conn.commit()
        except Exception as e:
            msg = [e]
        return msg
    def request(self,lst):
        res = []
        lst = X.parser(lst,';')
        
        for i in lst:
            res.append(self.request_line(i))
        return res
  
        