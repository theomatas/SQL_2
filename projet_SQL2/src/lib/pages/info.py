from tkinter import *

def main(self):
    self.clean()
    fen = self.fen
    canvas = self.canvas
    bouton = []
    patryck = PhotoImage(file= "../image/binary.gif")
    bouton.append(canvas.create_image(300, 300, image = patryck))
    canvas.image = patryck       
    bouton.append(canvas.create_rectangle( 25,25,575,490,  fill = "silver" ))
    bouton.append(Button(fen, text="Retour", command=self.fen_1,bg="orangered",font=('Helvetica', '10'), width = 25, height = 3))
    bouton.append(Button(fen, text="Relancer", command=self.reload,bg="orange",font=('Helvetica', '10'), width = 25, height = 3))
    txt = "Bienvenue sur notre application de gestion \nde planning.\n\nvous pouvez ici ajouter ou consulter les\ninformation contenue sur une BBD \
simplifiee\nsimulant celle d'une ecole.\n\n* cree par:\n - Theo Matas\n - Jean Panthou \n - Hanaa\n\n"
    if self.BDD:
        txt += "BDD prete et charger"
    else:
        txt += "BDD non trouve WAMP est-il allume ?"
    txt = txt.split('\n')
    for i in range(len(txt)):
        bouton.append(canvas.create_text( 35, i*30 + 50 , text = txt[i] , font=('Helvetica', '15'), fill = "red" ,  anchor= 'w'))
    for i in range(len(bouton)):
        try:
            bouton[i].place(x = 50 + (i-2)*250, y =   515 )
        except:
            pass    
    self.bouton = bouton