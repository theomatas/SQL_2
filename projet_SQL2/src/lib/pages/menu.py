from tkinter import *

def main(self):
    self.clean()
    bouton=[]
    canvas = self.canvas
    fen = self.fen
    patryck = PhotoImage(file= "../image/binary.gif")
    bouton.append(canvas.create_image(300, 300, image = patryck))
    canvas.image = patryck       
    bouton.append(canvas.create_rectangle( 50,25,550,225,  fill = "silver" ))
    bouton.append(Button(fen, text="Consulter le Planning", command= self.consulter,bg ="royalblue",font=('Helvetica', '10'), width = 25, height = 3))
    bouton.append(Button(fen, text="Editer le Planning", command=self.editer,bg="aquamarine",font=('Helvetica', '10'), width = 25, height = 3))
    bouton.append(Button(fen, text="Information", command=self.info,bg="goldenrod",font=('Helvetica', '10'), width = 25, height = 3))
    bouton.append(Button(fen, text="Quitter l'application", command=fen.quit,bg="orangered",font=('Helvetica', '10'), width = 25, height = 3))
    bouton.append(canvas.create_text( 300,125 , text = "MINI_PLANNING" , font=('Helvetica', '30'), fill = "red" ))
    for i in range(len(bouton)):
        try:
            bouton[i].place(x = 175 , y = i*85 + 75 )
        except:
            pass
    self.bouton = bouton