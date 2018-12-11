import lib.simple_fonction as X
import lib.creat_base as B
import lib.sql_fonction as SQL
import lib.interface_script as I
import lib.interface_graph as G
from tkinter import * 

fen = Tk()
canvas = Canvas(fen, width=600, height=600,bg="black")

def init():
    global Base, ACT
     
    try:
        Base, ACT = loader()
    except:
        ACT = G.new_fen(fen,canvas,Button, False)
    #print(effecteur())
    loop()
 
def loader():
    Base = B.BDD()
    cmd = """CREATE TABLE STATION 
        (ID INTEGER PRIMARY KEY, 
        CITY CHAR(20), 
        STATE CHAR(2), 
        LAT_N REAL, 
        LONG_W REAL);
        CREATE TABLE STAT 
        (ID INTEGER PRIMARY KEY, 
        CITY CHAR(20), 
        STATE CHAR(2), 
        LAT_N REAL, 
        LONG_W REAL);
        INSERT INTO STATION VALUES (13, 'Phoenix', 'AZ', 33, 112);
        INSERT INTO STATION VALUES (44, 'Denver', 'CO', 40, 105);
        INSERT INTO STATION VALUES (66, 'Caribou', 'ME', 47, 68);
        SHOW COLUMNS FROM station;
        SHOW TABLES;
        """
    #text = Base.request(cmd)
    #print(text)
    ACT = G.new_fen(fen,canvas,Button,Base)    
    return Base, ACT
    

def effecteur():
    res = I.listerner()
    if res[0] == 0:
        
        cmd = SQL.selector(res[1][0],res[1][1])
    if res[0] == 1:
        cmd = SQL.insertor(res[1][0],res[1][1])
    print (cmd)
    text = Base.request_line(cmd)
    return text

def loop():
    global Base, ACT
    if ACT.get_COM()[0] :
        fen.after(100,loop)
    elif ACT.get_COM()[1] != []:
        SQL.add_table(Base,ACT.get_COM()[1])
        ACT.reset_COM()
        ACT.table_set()
    else: 
        B = ACT
        init()
        B.clean()




init()
canvas.pack()
fen.mainloop()  



