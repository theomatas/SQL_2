from tkinter import *
from lib.input_area import input_text
from lib.text_area import display_text

def main(self):
    self.clean()
    self.reset_COM()
    bouton=[]
    canvas = self.canvas
    fen = self.fen
    patryck = PhotoImage(file= "../image/binary.gif")
    bouton.append(canvas.create_image(300, 300, image = patryck))
    canvas.image = patryck       
    
    if self.law == 3:
        bouton.append(canvas.create_rectangle( 50,25,550,225,  fill = "silver" ))
        bouton.append(Button(fen, text="Consulter le Planning", command= self.consulter,bg ="royalblue",font=('Helvetica', '10'), width = 25, height = 3))
        bouton.append(Button(fen, text="Editer le Planning", command=self.editer,bg="aquamarine",font=('Helvetica', '10'), width = 25, height = 3))
        bouton.append(Button(fen, text="Information", command=self.info,bg="goldenrod",font=('Helvetica', '10'), width = 25, height = 3))
        bouton.append(Button(fen, text="Quitter l'application", command=fen.quit,bg="orangered",font=('Helvetica', '10'), width = 25, height = 3))
    elif self.law == 2:
        bouton.append(canvas.create_rectangle( 50,25,550,225,  fill = "silver" ))
        bouton.append(Button(fen, text="Consulter le Planning", command= self.consulter,bg ="royalblue",font=('Helvetica', '10'), width = 25, height = 3))
        bouton.append(Button(fen, text="Editer le Planning", command=self.editer,bg="aquamarine",font=('Helvetica', '10'), width = 25, height = 3))
        bouton.append(Button(fen, text="Information", command=self.info,bg="goldenrod",font=('Helvetica', '10'), width = 25, height = 3))
        bouton.append(Button(fen, text="Quitter l'application", command=fen.quit,bg="orangered",font=('Helvetica', '10'), width = 25, height = 3))
    elif self.law == 1:
        bouton.append(canvas.create_rectangle( 50,25,550,225,  fill = "silver" ))
        bouton.append(Button(fen, text="Consulter le Planning", command= self.consulter,bg ="royalblue",font=('Helvetica', '10'), width = 25, height = 3))
        bouton.append(Button(fen, text="Information", command=self.info,bg="goldenrod",font=('Helvetica', '10'), width = 25, height = 3))
        bouton.append(Button(fen, text="Quitter l'application", command=fen.quit,bg="orangered",font=('Helvetica', '10'), width = 25, height = 3))    
    else:
        self.COM[1] = ["law"]
        bouton.append(canvas.create_rectangle( 50,25,550,500,  fill = "silver" ))
        bouton.append(Button(fen, text="Valider", command=self.load,bg="greenyellow",font=('Helvetica', '10'), width = 25, height = 3))
        bouton[-1].place(x = 65 , y = 400 )
        bouton.append(Button(fen, text="Information", command=self.info,bg="goldenrod",font=('Helvetica', '10'), width = 25, height = 3))
        bouton[-1].place(x = 305 , y = 400 )
        bouton.append(input_text(fen,210,300,20))
        self.COM[1].append(bouton[-1])
        
        
    bouton.append(canvas.create_text( 300,125 , text = "MINI_PLANNING" , font=('Helvetica', '30'), fill = "red" ))
    bouton.append(display_text(canvas,300,250,30))
    if self.law != 0:
        for i in range(len(bouton)):
            try:
                bouton[i].place(x = 175 , y = i*85 + 75 )
            except:
                pass
    else:
        bouton[-1].set_text("connectez vous !")

    self.bouton = bouton