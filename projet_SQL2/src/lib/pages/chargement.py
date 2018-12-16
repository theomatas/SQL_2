from tkinter import *

def main(self):
     self.clean()
     self.COM = [False,[]]
     bouton = []
     canvas = self.canvas
     fen = self.fen
     patryck = PhotoImage(file= "../image/chargement.gif")
     bouton.append(canvas.create_image(300, 300, image = patryck))
     canvas.image = patryck    
     self.bouton = bouton