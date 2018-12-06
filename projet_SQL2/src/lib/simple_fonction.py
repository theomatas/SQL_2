import os, os.path

def my_open(file_adresse):
    file_ = open(file_adresse, 'r')
    text = file_.read()
    file_.close()
    return text

def my_write(file_adresse, text):
    file_ = open(file_adresse, 'w')
    file_.write(text)
    file_.close()

def adresse():
    return os.path.dirname(__file__)

def lst_fichier(path):
    return os.listdir(path)

def removed(file_adresse):
    os.remove(file_adresse)
    
def parser(text,char):
    lst = []
    line = ""
    for char in text:
        if char != '\n':
            line += char
        if char == ';':
            lst.append(line)
            line = ""
    if line != "":
        lst.append(line)
    return lst


