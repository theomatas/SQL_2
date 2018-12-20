from tkinter import *
import calendar

def main(self):
    self.clean()
    bouton = []   
    day = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    hour = [8,10,12,14,16,18,20]
    canvas = self.canvas
    fen = self.fen
    data = self.data[1]
    student = self.law[2]
    for stud in data:
        if stud[0] == student:
            text = stud[4]
    patryck = PhotoImage(file= "../image/binary.gif")
    bouton.append(canvas.create_image(300, 300, image = patryck))
    canvas.image = patryck       
    bouton.append(canvas.create_rectangle( 25,25,575,490,  fill = "silver" ))
    bouton.append(Button(fen, text="semaine\nprecedant", command=self.moins,bg="dodgerblue",font=('Helvetica', '10'), width = 15, height = 3))    
    bouton.append(Button(fen, text="Retour", command=self.fen_1,bg="orangered",font=('Helvetica', '10'), width = 15, height = 3))
    bouton.append(Button(fen, text="semaine\nsuivante", command=self.plus,bg="lightgreen",font=('Helvetica', '10'), width = 15, height = 3))
    for i in range(len(bouton)):
        try:
            bouton[i].place(x = -300 + i * 175 , y = 500 )
        except:
            pass
    local_date = str(zero(self.date[0][0])) + "/" + str(zero(self.date[0][1])) + "/" + str(zero(self.date[0][2])) + " - "
    local_date += str(zero(self.date[1][0])) + "/" + str(zero(self.date[1][1])) + "/" + str(zero(self.date[1][2]))
    bouton.append(canvas.create_text( 300,80, text= local_date, font=('Helvetica', '15'), fill = "red" ))        
    x1,y1,x2,y2 = 30, 150 - 20  , 90 , 150 + 20  
    bouton.append(canvas.create_rectangle( x1,y1,x2,y2, fill = "red")) 
    for i in range(len(hour)):
        x1,y1,x2,y2 = 30, 150 - 20 + 42 * (i+1) , 90 , 150 + 20 + 42 * (i+1) 
        bouton.append(canvas.create_rectangle( x1,y1,x2,y2, fill = "palegreen"))        
        bouton.append(canvas.create_text( (x1+x2)//2, (y1+y2)//2, text= hour[i], font=('Helvetica', '8'), fill = "red" ))        
    for d in day:
        pos = day.index(d)
        x1,y1,x2,y2 = 93 + pos * 68, 150 - 20 , 158 + pos * 68 , 150 + 20
        bouton.append(canvas.create_rectangle( x1,y1,x2,y2, fill = "skyblue"))        
        bouton.append(canvas.create_text( (x1+x2)//2, (y1+y2)//2, text= d, font=('Helvetica', '8'), fill = "red" ))        
        for i in range(len(text)):
            nom = text[i][0]
            debut = str(zero(text[i][1][0])) + "H" + str(zero(text[i][1][1])) 
            fin = str(zero(text[i][2][0])) + "H" + str(zero(text[i][2][1]))
            jour = planning(text[i][6])
            posX = day.index(jour)
            posY = hour.index(text[i][1][0])
            date = str(zero(text[i][6][0])) + "/" + str(zero(text[i][6][1])) + "/" + str(zero(text[i][6][2]))
            x1,y1,x2,y2 = 95 + pos * 65, 42*posY + 192 - 20 , 155 + pos * 65  , 192 + 42*posY + 20
            if d == jour and date_in(self.date,text[i][6]):
                bouton.append(canvas.create_rectangle( x1,y1,x2,y2, fill = "khaki"))        
                bouton.append(canvas.create_text( (x1+x2)//2, (y1+y2)//2, text= nom, font=('Helvetica', '6'), fill = "red" ))    
    self.bouton = bouton
    
def zero(val):
    if val == 0:
        return "00"
    return val

def planning(date):
    days = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    return days[calendar.weekday(date[2] + 2000,date[1],date[0])]     

def date_in(date,day):
    
    jour = date[0][0] <= day[0] <= date[1][0]
    mois = date[0][1] <= day[1] <= date[1][1]
    an = date[0][2] <= day[2] <= date[1][2]
    return jour and mois and an