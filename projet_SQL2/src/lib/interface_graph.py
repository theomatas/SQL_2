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
import lib.pages.etudiant_planning as etudiant_planning
import lib.pages.poping as poping
import lib.toggle as toggle

class new_fen ():
       def __init__(self,fen,canvas,Button,BDD,law,data):
              self.fen = fen
              self.law = [law,None]
              self.canvas = canvas              
              self.COM = [True,[]]
              self.bouton = []
              self.BDD = BDD
              self.data = data
              self.date = [[17,12,18],[23,12,18]]
              self.mois = [31,28,31,30,31,30,31,31,30,31,30,31]
              self.table_set()
              self.event = []
              self.info_bouton = []
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
              fen_clean.main(self,self.bouton) 
       
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
              
       def load_insertion(self):
              if self.COM[1][0] != "insertion" and self.COM[1][0] != "remplacer":
                     self.COM[1] = ["insertion"] + self.COM[1]
              else:
                     self.COM[1][0] = "insertion"
              self.load()
              
       def load_remplace(self):
              if self.COM[1][0] != "insertion" and self.COM[1][0] != "remplacer":
                     self.COM[1] = ["remplacer"] + self.COM[1]
              else:
                     self.COM[1][0] = "remplacer"
              self.load()
              
# recuperer le nom des tables et ceux de leurs colonnes.
       
       def table_set(self):
              self.table = table.main(self)      
       
       def get_table(self):
              return self.table
              
# donne des tables
       
       def set_data(self,data):
              self.data = data
              
       def get_data(self):
              return self.data
       
# consulter les tables
              
       def consulter(self):
              table_display.main(self)            
              
       def select(self,num):
              self.COM = [False,["selection" ,self.table[num][0]]]
              
       def select_etudiant(self):
              etudiant_planning.main(self)
              
       def select_tab(self,text):
              table_display_item.main(self,text)
              
# editer les tables
              
       def editer(self):
              edit.main(self)
             
       def insert(self,table):
              edit_table.main(self,table)

# autorisation

       def get_law(self):
              return self.law

       def set_law(self,value):
              self.law = value
  
# pop_up

       def pop_up(self,text):
              toggle.invisible(self,self.bouton)
              poping.main(self,text)
              
       def clean_pop(self):
              fen_clean.main(self,self.event) 
              toggle.visible(self,self.bouton)
              self.event = []
              
       def get_event(self):
              return self.event
              
              
              
# actualisation des dates

       def plus(self):
              for i in [0,1]:
                     self.date[i][0] += 7
                     if self.date[i][0] > self.mois[self.date[i][1] - 1]:
                            self.date[i][0] -= self.mois[self.date[i][1] - 1]
                            self.date[i][1] += 1
                     if self.date[i][1] > 12:
                            self.date[i][1] = 1
                            self.date[i][2] += 1
              self.select_etudiant()

       def moins(self):
              for i in [0,1]:
                     self.date[i][0] -= 7
                     if self.date[i][0] < 1:
                            self.date[i][1] -= 1
                            if self.date[i][1] >= 1:
                                   self.date[i][0] += self.mois[(self.date[i][1]) - 1]
                     if self.date[i][1] < 1:
                            self.date[i][1] = 12
                            self.date[i][2] -= 1
                            self.date[i][0] += 31
              self.select_etudiant()