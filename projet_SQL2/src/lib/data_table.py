import lib.sql_fonction as SQL
import lib.pages.table as T
import lib.simple_fonction as X

def main(Base):
    data = []
    for table in Base.request_line("SHOW TABLES;"):
        data.append(Base.request_line(SQL.selector(table[0], "*")))
    table = T.table(Base)
    for i in range(len(table)):
        data[i] = [table[i][0],table[i][1],data[i]]
    etudiant_data = etudiant(data)
    etudiant_data = etudiant_cour(Base,etudiant_data)
    cours_data = cours(data)
    etudiant_data = my_cour(cours_data,etudiant_data)
    return [cours_data,etudiant_data]
        
def cours(data):
    cours = []
    for table_num in range(len(data)):
        table_info = data[table_num]
        if table_info[0] == "cours":
            for i in range(len(table_info[2])):
                C = []
                for j in range(len(data[table_num][2][i])):
                    val = data[table_num][2][i][j]
                    if j == 1 or j == 2 or j == 6:
                        try:
                            C.append(parser(val))
                        except:
                            break
                    else:
                        C.append(val)
                    if j == 6:
                        cours.append(C)      
    return tri_cour(cours)
    
def etudiant(data):
    etudiant = []
    for table_num in range(len(data)):
        table_info = data[table_num]
        if table_info[0] == "etudiant":
            for i in table_info[2]:
                sto = []
                for j in i[0:3]:
                    sto.append(j)
                etudiant.append(sto)
    return etudiant

def etudiant_cour(BDD,etudiant):
    for i in range(len(etudiant)):
        text = BDD.request_line("SELECT DISTINCT(NOMGRP) FROM GRP, ETUDIANT WHERE GRP.MATRICULEE \
    = ETUDIANT.MATRICULEE AND ETUDIANT.MATRICULEE = " + etudiant[i][0] + ";" )
        M = []
        for j in text:
            M.append(j[0])
        etudiant[i].append(M)
    return etudiant

def my_cour(cours,etudiant_data):
    for i in range(len(etudiant_data)):
        M = []
        for classe in cours:
            if X.is_inside(etudiant_data[i][3],classe[5]):
                M.append(classe)
        etudiant_data[i].append(M)
    return etudiant_data

def parser(A):
    A = A.split('-')
    for i in range(len(A)):
        A[i] = int(A[i])
    return A
        
        
def tri_cour(cour):
    e = True
    while e:
        e = False
        for i in range(len(cour) - 1 ):
            if bool_cour(cour[i+1],cour[i]):
                cour[i+1],cour[i] = cour[i],cour[i+1]
                e = True
    return cour
            
def bool_cour(A,B):
    if A[6][2] < B[6][2]:
        return True
    if A[6][1] < B[6][1]:
        return True
    if A[6][0] < B[6][0]:
        return True   
    if A[1][0] < B[1][0]:
        return True   
    if A[1][1] < B[1][1]:
        return True  
    return False
    
    