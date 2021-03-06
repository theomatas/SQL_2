from tkinter import *
from lib.input_area import input_text
from lib.text_area import display_text

def main(self,table):
    self.clean()
    bouton = []
    self.COM[1] = []
    canvas = self.canvas
    fen = self.fen
    patryck = PhotoImage(file= "../image/binary.gif")
    bouton.append(canvas.create_image(300, 300, image = patryck))
    canvas.image = patryck       
    bouton.append(canvas.create_rectangle( 25,20,575,500,  fill = "silver" ))
     
    bouton.append(Button(fen, text="Retour", command=self.editer,bg="orangered",font=('Helvetica', '10'), width = 12, height = 3))
    bouton.append(Button(fen, text="Inserer", command=self.load_insertion,bg="dodgerblue",font=('Helvetica', '10'), width = 12, height = 3))   
    bouton.append(Button(fen, text="Remplacer", command=self.load_remplace,bg="lightgreen",font=('Helvetica', '10'), width = 12, height = 3))
    bouton.append(Button(fen, text="Suprimer", command=self.load_drop,bg="salmon",font=('Helvetica', '10'), width = 12, height = 3))
    for i in range(len(bouton)):
        try:
            bouton[i].place(x = -200 + i * 125 , y = 520 )
        except:
            pass
    self.COM[1].append(str(self.table[table][0]))
    for i in range(len(self.table[table][1])):
        x1,y1,x2,y2 = 50 , 22*i + 50 - 10 , 70 + 200  , 50 + 22*i + 10
        bouton.append(canvas.create_rectangle( x1,y1,x2,y2, fill = "khaki"))
        opt = ""
        if str(self.table[table][1][i])[0] == 'H':
            opt = " HH-MM"
        if str(self.table[table][1][i])[0:4] == 'Date':
            opt = " JJ-MM-AA"        
        bouton.append(canvas.create_text( (x1+x2)//2, (y1+y2)//2, text=str(self.table[table][1][i]) + opt, font=('Helvetica', '10'), fill = "red" ))
        bouton.append(input_text(fen,x1+250,y1,30))
        self.COM[1].append(bouton[-1])
    bouton.append(display_text(canvas,300,490,9))
    self.bouton = bouton