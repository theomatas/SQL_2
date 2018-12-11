from tkinter import *

def main(self):
    table = []
    if self.BDD:
        for tables in self.BDD.request_line("SHOW TABLES;"):
            clmn_lst = []
            for clmn in  self.BDD.request_line("SHOW COLUMNS FROM " + tables[0] + ";"):
                clmn_lst.append(clmn[0])
            table.append([tables[0],clmn_lst])  
    self.table = table      