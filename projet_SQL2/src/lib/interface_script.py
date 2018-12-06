def listerner():
    val = 0
    cmd_lst = [["table","Colone"],["table","valeur"]]
    while not val:
        print( "choisir commande" )
        print( "1- SELECT" )
        print( "2- INSERT" )
        try:
            val = int(input())
        except:
            print("mauvaise commande")
    val -= 1
    data = []
    for i in cmd_lst[val]:
        brut = input(i + " : " )
        data.append(brut)
    return [val,data]
        
    
    