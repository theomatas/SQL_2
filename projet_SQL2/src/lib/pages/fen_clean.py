from tkinter import *


def main(self,M):
    self.unload()
    for i in M:
        try:
            i.destroy()
        except:
            try:
                i.get_ent().destroy()
            except:
                try:
                    self.canvas.delete(i.get_ent())
                except:
                    self.canvas.delete(i)    
  