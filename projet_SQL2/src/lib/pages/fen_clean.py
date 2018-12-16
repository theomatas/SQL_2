from tkinter import *


def main(self):
    self.unload()
    for i in self.bouton:
        try:
            i.destroy()
        except:
            try:
                i.get_ent().destroy()
            except:
                self.canvas.delete(i)    
  