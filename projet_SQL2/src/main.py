import lib.simple_fonction as X
import lib.creat_base as B
import lib.sql_fonction as SQL
import lib.interface_script as I
import lib.interface_graph as G
import lib.pass_word as P
import lib.data_table as D
from tkinter import * 

def fen_init():
    global fen, canvas
    fen = Tk()
    canvas = Canvas(fen, width=600, height=600,bg="black") 

def init():
    global Base, ACT
    try:
        Base, ACT = loader()
    except:
        ACT = G.new_fen(fen,canvas,Button, False,0,[])
        ACT.set_COM("no signal")
    loop()
 
def loader(): 
    Base = B.BDD()
    data = D.main(Base)
    ACT = G.new_fen(fen,canvas,Button,Base,0,data)    
    return Base, ACT

def loop():
    global Base, ACT, data
    if ACT.get_COM()[0]: 
        if test_connection():
            data = D.main(Base)
            #print(data)
            ACT.set_data(data)
        fen.after(100,loop)
    elif ACT.get_COM()[1] != [] and ACT.get_COM()[1] != "no signal":
        if ACT.get_COM()[1][0] == "insertion":
            text = SQL.add_table(Base,ACT.get_COM()[1][1:])
            ACT.last().set_text(text)
            ACT.unload()
            fen.after(100,loop)
        if ACT.get_COM()[1][0] == "selection":
            text = SQL.see_table(Base,ACT.get_COM()[1])
            ACT.select_tab(text)
            ACT.reset_COM()
            fen.after(100,loop)     
        if ACT.get_COM()[1] != [] and ACT.get_COM()[1][0] == "law":
            cmd = ACT.get_COM()[1]
            text = P.main(cmd[1].get_text(),ACT.get_data()[1])
            print(text)
            if not text:
                ACT.last().set_text("mot de pass inexistant")
            else:
                ACT.set_law(text)
                ACT.fen_1()
            ACT.unload()
            fen.after(1000,loop)
    else: 
        re_init()
        
def re_init():
    
    B = ACT
    init()
    B.clean()
    
def test_connection():
    
    COM = ACT.get_COM()[1]
    
    try:
        text = SQL.test(Base)
        if text[0:2] == "@E" and (COM == [] or COM != "no signal"):
            ACT.set_COM("no signal")
            re_init()
            return False
        else:
            return True
    except:
        if COM == [] or COM != "no signal":
            re_init()  
            return False

fen_init()
init()
canvas.pack()
fen.mainloop()  



