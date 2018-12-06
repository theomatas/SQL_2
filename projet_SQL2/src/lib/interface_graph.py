from tkinter import * 

class new_fen ():
       def __init__(self,fen,canvas,Button,BDD):
              self.fen = fen
              self.canvas = canvas              
              self.COM = 0
              self.bouton = []
              self.fen_1()
              self.BDD = BDD
              
       def fen_1(self):
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
       def consulter(self):
              self.COM = 1
       def editer(self):
              self.COM = 2
       def clean(self):
              for i in self.bouton:
                     try:
                            self.canvas.delete(i)
                     except:
                            i.destroy()                      
       def info(self):
              self.clean()
              bouton = []
              canvas = self.canvas
              fen = self.fen
              patryck = PhotoImage(file= "../image/binary.gif")
              bouton.append(canvas.create_image(300, 300, image = patryck))
              canvas.image = patryck       
              bouton.append(canvas.create_rectangle( 25,25,575,490,  fill = "silver" ))
              bouton.append(Button(fen, text="Fermer", command=self.fen_1,bg="orangered",font=('Helvetica', '10'), width = 25, height = 3))
              txt = "Bienvenue sur notre application de gestion \nde planning.\n\nvous pouvez ici ajouter ou consulter les\ninformation contenue sur une BBD \
simplifiee\nsimulant celle d'une ecole.\n\n* cree par:\n - Theo Matas\n - Jean Panthou \n - Hanaa\n\n"
              if self.BDD:
                     txt += "BDD prete et charger"
              else:
                     txt += "BDD non trouve WAMP est-il allume"
              txt = txt.split('\n')
              for i in range(len(txt)):
                     bouton.append(canvas.create_text( 35, i*30 + 50 , text = txt[i] , font=('Helvetica', '15'), fill = "red" ,  anchor= 'w'))
              for i in range(len(bouton)):
                     try:
                            bouton[i].place(x = 175 , y = i*85 + 340 )
                     except:
                            pass
              self.bouton = bouton
       def get_COM(self):
              return self.COM