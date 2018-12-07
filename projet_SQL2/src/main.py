import lib.simple_fonction as X
import lib.creat_base as B
import lib.sql_fonction as SQL
import lib.interface_script as I
import lib.interface_graph as G
from tkinter import * 


def init():
    global fen, canvas, Base, ACT
    fen = Tk()
    canvas = Canvas(fen, width=600, height=600,bg="black") 
    try:
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
        text = Base.request(cmd)
        print(text)
        ACT = G.new_fen(fen,canvas,Button,Base)
    except:
        ACT = G.new_fen(fen,canvas,Button, False)
    #print(effecteur())
    loop()
    
    

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
    fen.after(100,loop)




init()
canvas.pack()
fen.mainloop()  



