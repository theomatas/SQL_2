from tkinter import *

class input_text:
    def __init__(self,fen,X,Y,L):
        self.text = StringVar()
        self.text_zone = Entry(fen, textvariable = self.text, width=L)
        self.text_zone.place(x = X, y = Y)
    def get_text(self):
        return self.text.get()
    def get_ent(self):
        return self.text_zone