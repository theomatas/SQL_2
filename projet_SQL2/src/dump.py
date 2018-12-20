def main(self):
    if not self.BDD:
        return self.info()
    self.clean()
    bouton = []
    canvas = self.canvas
    fen = self.fen
    patryck = PhotoImage(file= "../image/binary.gif")
    bouton.append(canvas.create_image(300, 300, image = patryck))
    canvas.image = patryck       
    bouton.append(canvas.create_rectangle( 25,25,575,490,  fill = "silver" ))
    bouton.append(Button(fen, text="Retour", command=self.fen_1,bg="orangered",font=('Helvetica', '10'), width = 25, height = 3))
    for i in range(len(bouton)):
        try:
            bouton[i].place(x = 175 , y = i*85 + 340 )
        except:
            pass              
    for i in range(len(self.table)):
        bouton.append(Button(fen, text=str(self.table[i][0]), command= lambda i=i: self.insert(i), bg="khaki",font=('Helvetica', '10'), width = 15, height = 2))
        bouton[-1].pack()
        bouton[-1].place(x = 50 + 180 * (i%3)  , y = i//3*70 + 100 )

    bouton.append(canvas.create_text( 300,50 , text = "Selectioner une table" , font=('Helvetica', '25'), fill = "red" ))                                          

    self.bouton = bouton
    
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
    
    
    
def effecteur():
    res = I.listerner()
    if res[0] == 0:
        
        cmd = SQL.selector(res[1][0],res[1][1])
    if res[0] == 1:
        cmd = SQL.insertor(res[1][0],res[1][1])
    text = Base.request_line(cmd)
    return text


#DELETE FROM `table`
#WHERE condition