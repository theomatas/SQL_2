from tkinter import * 

class new_fen ():
       def __init__(self,fen,canvas,Button,BDD):
              self.fen = fen
              self.canvas = canvas              
              self.COM = 0
              self.bouton = []
              self.BDD = BDD
              self.table_set()
              self.fen_1()
              
              
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
              if not self.BDD:
                     return self.info()
              self.clean()
              bouton = []
              canvas = self.canvas
              fen = self.fen
              patryck = PhotoImage(file= "../image/binary.gif")
              bouton.append(canvas.create_image(300, 300, image = patryck))
              canvas.image = patryck       
              bouton.append(canvas.create_rectangle( 25,25,575,490,  fill = "silver" ))
              bouton.append(Button(fen, text="Retour", command=self.fen_1,bg="orangered",font=('Helvetica', '10'), width = 25, height = 3))
              for i in range(len(bouton)):
                     try:
                            bouton[i].place(x = 175 , y = i*85 + 340 )
                     except:
                            pass

              for i in range(len(self.table)):
                     bouton.append(Button(fen, text=str(self.table[i][0]), command= lambda i=i: self.select(i), bg="khaki",font=('Helvetica', '10'), width = 15, height = 2))
                     bouton[-1].pack()
                     bouton[-1].place(x = 50 + 180 * (i%3)  , y = i//3*70 + 100 )

              self.bouton = bouton
       def editer(self):
              if not self.BDD:
                     return self.info()
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
              bouton.append(Button(fen, text="Retour", command=self.fen_1,bg="orangered",font=('Helvetica', '10'), width = 25, height = 3))
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
                            bouton[i].place(x = 175 , y = i*85 + 340 )
                     except:
                            pass
              self.bouton = bouton
       def get_COM(self):
              return self.COM
       
       def table_set(self):
              table = []
              if self.BDD:
                     for tables in self.BDD.request_line("SHOW TABLES;"):
                            clmn_lst = []
                            for clmn in  self.BDD.request_line("SHOW COLUMNS FROM " + tables[0] + ";"):
                                   clmn_lst.append(clmn[0])
 
                            
                            table.append([tables[0],clmn_lst])
                                   
              self.table = table      
       def select(self,num):
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

              for i in range(len(self.table[num][1])):
                     bouton.append(Button(fen, text=str(self.table[num][1][i]), bg="khaki",font=('Helvetica', '10'), width = 15, height = 2))
                     bouton[-1].pack()
                     bouton[-1].place(x = 50 + 180 * (i%3)  , y = i//3*70 + 100 )

              self.bouton = bouton