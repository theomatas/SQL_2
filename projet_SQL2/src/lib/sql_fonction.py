
def selector(table,clmn):
    return "SELECT " + str(clmn) + " FROM " + str(table) + ";"

def insertor(table,data):
    return "INSERT INTO " + str(table) + " VALUES (" + str(data) + " );"
    
    
    