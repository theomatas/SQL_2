from tkinter import *

def main(self,text):
    fen = self.fen
    canvas = self.canvas
    event = [] 
    event.append(canvas.create_rectangle( 10,10,590,590,  fill = "lightgrey" , width = 5))
    canvas.tag_raise(event[-1])
    event.append(Button(fen, text="fermer", command=self.clean_pop,bg="red",font=('Helvetica', '10'), width = 25, height = 3))    
    event[-1].place(x = 175, y =   515 )
   
    event.append(canvas.create_text( 300,30 , text = "__Attention__" , font=('Helvetica', '20'), fill = "red"))
    for i in range(len(text)):
        event.append(canvas.create_text( 20, i*40 + 100 , text = text[i] , font=('Helvetica', '10'), fill = "red" ,  anchor= 'w'))
    self.event = event