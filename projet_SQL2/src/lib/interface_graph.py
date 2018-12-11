from tkinter import * 
import lib.pages.menu as menu
import lib.pages.info as info
import lib.pages.table_display as table_display
import lib.pages.chargement as chargement
import lib.pages.table as table
import lib.pages.edit as edit
import lib.pages.edit_table as edit_table

class new_fen ():
       def __init__(self,fen,canvas,Button,BDD):
              self.fen = fen
              self.canvas = canvas              
              self.COM = [True,[]]
              self.bouton = []
              self.BDD = BDD
              self.table_set()
              self.fen_1()
              
       def fen_1(self):
              menu.main(self)   
              
       def consulter(self):
              table_display.main(self)
              
       def editer(self):
              edit.main(self)
             
              
       def clean(self):
              for i in self.bouton:
                     try:
                            i.destroy()
                     except:
                            try:
                                   i.get_ent().destroy()
                            except:
                                   self.canvas.delete(i) 
       def info(self):
              info.main(self)   
              
       def get_COM(self):
              return self.COM
       
       def reset_COM(self):
              self.COM = [True,[]]
       
       def reload(self):
              chargement.main(self)
              
       def load(self):
              self.COM[0] = False
              
       def table_set(self):
              table.main(self)
    
       def insert(self,table):
              edit_table.main(self,table)
              
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
                    
              bouton.append(canvas.create_text( 300,50 , text = "Selectioner une colone" , font=('Helvetica', '25'), fill = "red" )) 
              
              self.bouton = bouton
