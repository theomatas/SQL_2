import lib.sql_fonction as SQL


def main(base,data):
    sup = []
    sup += place(base)
    sup += time_simul(base,data)
    sup += time_hour(base,data)
    sup += time_simul_eleve(base,data)
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
    for i in range(len(data[1])):        
        for A in data[1][i][4]:
            count = 0
            dej12 = False
            dej14 = False
            for B in data[1][i][4]:
                if not is_inside(lst,A) and not is_inside(lst,B):
                    if A != B and A[6] == B[6] and not is_inside(lst,B):
                        count += 1
                    if A != B and A[6] == B[6] and count >= 4 and not is_inside(lst,B):
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
    
def is_inside(lst,char):
    for i in lst:
        if i == char:
            return True
    return False
    
def bool_cour(A,B):
    if A[6][2] != B[6][2]:
        return False
    if A[6][1] != B[6][1]:
        return False
    if A[6][0] != B[6][0]:
        return False   
    if A[1][0] != B[1][0]:
        return False   
    if A[1][1] != B[1][1]:
        return False  
    return True