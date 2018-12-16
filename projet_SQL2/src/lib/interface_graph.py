from tkinter import * 
import lib.pages.menu as menu
import lib.pages.info as info
import lib.pages.table_display as table_display
import lib.pages.chargement as chargement
import lib.pages.table as table
import lib.pages.edit as edit
import lib.pages.edit_table as edit_table
import lib.pages.table_display_item as table_display_item
import lib.pages.fen_clean as fen_clean

class new_fen ():
       def __init__(self,fen,canvas,Button,BDD,law):
              self.fen = fen
              self.law = law
              self.canvas = canvas              
              self.COM = [True,[]]
              self.bouton = []
              self.BDD = BDD
              self.table_set()
              self.fen_1()
              
# fenetre d'acceuil.

       def fen_1(self):
              menu.main(self)   
              
# fenetre d'information et hors connection.
              
       def info(self):
              info.main(self)      
              
# relance une nouvelle connection.
              
       def reload(self):
              chargement.main(self)       
              
# gestion des elements de l'interface.
              
       def clean(self):            
              fen_clean.main(self) 
       
       def last(self):
              return self.bouton[-1]
       
       
# gestion de COM varible gerant la communication interface/main (BBD).
       
       def get_COM(self):
              return self.COM
       
       def reset_COM(self):
              self.COM = [True,[]]
              
       def load(self):
              self.COM[0] = False
              
       def unload(self):
              self.COM[0] = True
              
       def set_COM(self,COM):
              self.COM[1] = COM
              
# recuperer le nom des tables et ceux de leurs colonnes.
       
       def table_set(self):
              table.main(self)       
              
# consulter les tables
              
       def consulter(self):
              table_display.main(self)            
              
       def select(self,num):
              self.COM = [False,["selection" ,self.table[num][0]]]
              
       def select_tab(self,text):
              table_display_item.main(self,text)
              
# editer les tables
              
       def editer(self):
              edit.main(self)
             
       def insert(self,table):
              edit_table.main(self,table)

# autorisation

       def set_law(self,value):
              self.law = value
              
       