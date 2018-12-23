import csv
import lib.simple_fonction as X



def main(name,data,clmn):  
    filename = X.adresse()+ "//..//..//csv_planning_eleve//planning" + clean(name)  + ".csv"
    s = ";".join(clmn) + '\n'

    for ligne in data:
        s += dateforme(ligne) + '\n'
    X. my_write(filename,s)
        
        
def clean(lst):
    s = ""
    for i in lst:
        if i == ' ':
            s += '_'
        else:
            s += i
    return s


def zero(val):
    if val == 0:
        return "00"
    if val < 10:
        return "0" + str(val)
    return str(val)

def dateforme(ligne):
    debut = str(zero(ligne[1][0])) + "H" + str(zero(ligne[1][1])) 
    fin = str(zero(ligne[2][0])) + "H" + str(zero(ligne[2][1]))    
    date = str(zero(ligne[6][0])) + "/" + str(zero(ligne[6][1])) + "/" + str(zero(ligne[6][2]))
    ligne = ligne[0] +';'+ debut +';'+  fin +';'+  ligne[3] +';'+  ligne[4] +';'+  ligne[5] +';'+  date
    return ligne