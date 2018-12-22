from tkinter import *

def invisible(self,lst):
    for ent in lst:
        try:
            self.info_bouton.append(ent.place_info())
            ent.place_forget()
        except:
            pass
            
def visible(self,lst):
    for ent in lst:
        try:
            ent.place_info()
            ent.place(self.info_bouton.pop(0))
        except:
            pass