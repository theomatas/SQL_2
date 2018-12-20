def main(text,etudiant):
    try:
        return [["prof","admin"].index(text) + 2, text]
    except:
        try:
            matricul = etudiant[matricule(etudiant).index(text)][0]
            nom = etudiant[matricule(etudiant).index(text)][1]
            prenom = etudiant[matricule(etudiant).index(text)][2]
            return [1,prenom + " " + nom, matricul]
        except:
            return False

def matricule(etudiant):
    M = []
    for i in etudiant:
        M.append(i[0])
    return M