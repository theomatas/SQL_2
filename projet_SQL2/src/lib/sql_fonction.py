def selector(table,clmn):
    return "SELECT " + str(clmn) + " FROM " + str(table) + ";"

def insertor(table,data):
    return "INSERT INTO " + str(table) + " VALUES (" + str(data) + " );"

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
    print(cmd)
    text = Base.request(cmd)
    print(text)    
    
    
    