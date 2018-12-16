def main(text):
    try:
        return ["etudiant","prof","admin"].index(text) + 1
    except:
        return False
    