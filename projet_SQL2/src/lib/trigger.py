import lib.sql_fonction as SQL
import calendar
import lib.planning_calcule as P
import copy

def main(base,data):
    sup = []
    sup += place(base)
    sup += time_simul(base,data)
    sup += time_hour(base,data)
    sup += time_simul_eleve(base,data)
    sup += fill(base,data)
    return sup

def place(base):
    sup = []
    text = base.request_line("SELECT Q.CodeC FROM (SELECT CodeC, COUNT(grp.NomGRP) as val, nb_places FROM salle, cours\
    , grp WHERE grp.NomGRP = cours.NomGRP AND salle.CodeS = cours.CodeS GROUP BY CodeC) as Q WHERE Q.nb_places < Q.val")
    for table in text:
        data = "Cours " + table[0] + " trop d'etudiant pour la salle.\n"
        data += base.request_line(SQL.droper("cours","CodeC = '" + table[0] + "'") )
        sup.append(data)
    return sup

def time_simul(base,data):
    sup = []
    lst = []
    hour = ['8','10','12','14','16','18']
    for A in data[0]:
        for B in data[0]:
            if not is_inside(lst,A) and not is_inside(lst,B):
                if A != B and A[1:] == B[1:] and not is_inside(lst,B):
                    out = "Cours " + B[0] + " meme prof, date ou groupe qu'un autre cour\n"
                    out += base.request_line(SQL.droper("cours","CodeC = '"  + B[0] + "'") )
                    sup.append(out)
                    lst.append(B)
    return sup

    

def fill(base,data):
    lst = get_table(base)
    sup = []
    for A in data[0]:
        if not is_inside(lst[0],A[3]) or not is_inside(lst[1],A[4]) or not is_inside(lst[2],A[5]):
            out = "Cours " + A[0] + " pas de groupe, salle ou prof\n"
            out += base.request_line(SQL.droper("cours","CodeC = '"  + A[0] + "'") )
            sup.append(out)
    return sup

def time_hour(base,data):
    sup = []
    hour = [8,10,12,14,16,18]
    for A in data[0]:
            if  A[1][0] + 1 != A[2][0] or A[1][1] != 0 or A[2][1] != 45 :
                out = "Cours " + A[0] + " les heures ne respectent pas les creneaux\n"
                out += base.request_line(SQL.droper("cours","CodeC = '"  + A[0] + "'") )
                sup.append(out)
    return sup

def time_simul_eleve(base,data):
    sup = []
    lst = []
    day = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    for i in range(len(data[1])):        
        for A in data[1][i][4]:
            count_day = 0
            count_week = 0
            dej12 = False
            dej14 = False
            date = creat_date(A[6])
            if planning(A[6]) == "dimanche":
                out = "Cours " + A[0] + " pas le dimanche !!!\n"
                out += base.request_line(SQL.droper("cours","CodeC = '"  + A[0] + "'") )    
                sup.append(out)
                lst.append(A)               
            for B in data[1][i][4]:
                if not is_inside(lst,A) and not is_inside(lst,B):
                    if A != B and A[6] == B[6] and not is_inside(lst,B):
                        count_day += 1
                    if A != B and date_in(date,B[6]) and not is_inside(lst,B):
                        count_week += 1
                    if A != B and date_in(date,B[6]) and count_week >= 15 and not is_inside(lst,B):
                        out = "Cours " + B[0] + " trop d'heure pour un eleve en une semaine\n"
                        out += base.request_line(SQL.droper("cours","CodeC = '"  + B[0] + "'") )    
                        sup.append(out)
                        lst.append(B)    
                    if A != B and A[6] == B[6] and count_day >= 4 and not is_inside(lst,B):
                        out = "Cours " + B[0] + " trop d'heure pour un eleve en une journee\n"
                        out += base.request_line(SQL.droper("cours","CodeC = '"  + B[0] + "'") )    
                        sup.append(out)
                        lst.append(B)
                    if A[6] == B[6] and B[1][0] == 12 and not is_inside(lst,B):
                        dej12 = True
                    if A[6] == B[6] and B[1][0] == 14 and not is_inside(lst,B):
                        dej14 = True    
                    if dej14 and dej12:
                        out = "Cours " + B[0] + " bloque une pause dej\n"
                        out += base.request_line(SQL.droper("cours","CodeC = '"  + B[0] + "'") )
                        sup.append(out)
                        lst.append(B)                    
                    if A != B and A[1:3] == B[1:3] and A[6] == B[6] and not is_inside(lst,B):
                        out = "Cours " + B[0] + " meme creneau qu'un autre cour pour un eleve\n"
                        out += base.request_line(SQL.droper("cours","CodeC = '"  + B[0] + "'") )
                        sup.append(out)
                        lst.append(B)
    return sup

def planning(date):
    days = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    return days[calendar.weekday(date[2] + 2000,date[1],date[0])]   

def date_in(date,day):
    jour = date[0][0] <= day[0] <= date[1][0]
    mois = date[0][1] <= day[1] <= date[1][1]
    an = date[0][2] <= day[2] <= date[1][2]
    return jour and mois and an

def creat_date(date):
    debut = copy.deepcopy(date)
    fin = copy.deepcopy(date)
    while planning(debut) != "lundi":
        debut = P.moins_day(debut)
    while planning(fin) != "dimanche":
        fin = P.plus_day(fin)
    return [debut,fin]
    
def get_table(base):
    M = []
    data = []
    cmd = SQL.selector("salle","*")
    text = base.request_line(cmd)
    for i in text:
        data.append(i[0])
    M.append(data)
    data = []
    cmd = SQL.selector("professeur","*")
    text = base.request_line(cmd)
    for i in text:
        data.append(i[0])
    M.append(data)
    data = []
    cmd = SQL.selector("grp","*")
    text = base.request_line(cmd)
    for i in text:
        data.append(i[1]) 
    M.append(data)
    return M
    
def is_inside(lst,char):
    for i in lst:
        if i == char:
            return True
    return False
    
