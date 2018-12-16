from tkinter import *

class display_text:
    def __init__(self,canvas,X,Y,size):
        self.size = size
        self.X,self.Y = X,Y
        self.canvas = canvas
        
    def set_text(self,txt):
        X,Y = self.X,self.Y 
        try:
            self.canvas.delete(self.text_zone)
        except:
            pass
        if txt[0:2] == "@E":
            self.text_zone = self.canvas.create_text( X,Y, text= txt[4:]  , font=('Helvetica', str(self.size)), fill = "red" )
        else:
            self.text_zone = self.canvas.create_text( X,Y, text= txt  , font=('Helvetica', str(self.size)), fill = "blue" )
            
    def get_ent(self):
        return self.text_zone
    
    