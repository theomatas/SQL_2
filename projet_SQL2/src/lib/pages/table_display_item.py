from tkinter import *

def main(self,text):
    self.clean()
    bouton = []
    canvas = self.canvas
    fen = self.fen
    patryck = PhotoImage(file= "../image/binary.gif")
    bouton.append(canvas.create_image(300, 300, image = patryck))
    canvas.image = patryck       
    bouton.append(canvas.create_rectangle( 25,25,575,490,  fill = "silver" ))
    bouton.append(Button(fen, text="Retour", command=self.consulter,bg="orangered",font=('Helvetica', '10'), width = 25, height = 3))
    for i in range(len(bouton)):
        try:
            bouton[i].place(x = 175 , y = i*85 + 340 )
        except:
            pass
    for i in range(len(text)):
        x1,y1,x2,y2 = 40 , 22*i + 50 - 10 , 40 + 200  , 50 + 22*i + 10
        bouton.append(canvas.create_rectangle( x1,y1,x2,y2, fill = "khaki"))
        bouton.append(canvas.create_text( (x1+x2)//2, (y1+y2)//2, text= text[i] , font=('Helvetica', '10'), fill = "red" ))    
    self.bouton = bouton