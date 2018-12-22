def selector(table,clmn):
    return "SELECT " + str(clmn) + " FROM " + str(table) + ";"

def insertor(table,data):
    return "INSERT INTO " + str(table) + " VALUES (" + str(data) + " );"

def droper(table,data):
    return "DELETE FROM " + str(table) + " WHERE " + str(data) + ";"

def add_table(Base,lst):
    table = lst[0]
    data = ""
    for i in lst[1:]:
        value = i.get_text()
        try:
            int(value)
            data += value
        except:
            data += "'" + value + "'"
        data += ", "
        
    data = data[:-2]
    cmd = insertor(table,data)
    text = Base.request_line(cmd)
    return text    

def remplace_table(Base,lst,all_table):
    table = lst[0]
    ind = 0
    for i in range(len(all_table)):
        if all_table[i][0] == table:
            ind = i
    clmn = all_table[ind][1][0]
    data = lst[1].get_text()
    cmd = droper(table, str(clmn) + " = '"  + data + "'")
    text = Base.request_line(cmd)
    return add_table(Base,lst)   

def drop_table(Base,lst,all_table):
    table = lst[0]
    ind = 0
    for i in range(len(all_table)):
        if all_table[i][0] == table:
            ind = i
    clmn = all_table[ind][1][0]
    data = lst[1].get_text()
    cmd = droper(table, str(clmn) + " = '"  + data + "'")
    text = Base.request_line(cmd)
    return text  
    
def see_table(Base,lst):
    cmd = selector(lst[1],"""*""")
    text = Base.request_line(cmd)
    return text    
    
def test(Base):
    cmd = selector("""salle""","""*""")
    text = Base.request_line(cmd)
    return text      
    