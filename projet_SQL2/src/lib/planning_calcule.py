mois = [31,28,31,30,31,30,31,31,30,31,30,31]

def plus(self):
    for i in [0,1]:
        self.date[i][0] += 7
        if self.date[i][0] > mois[self.date[i][1] - 1]:
            self.date[i][0] -= mois[self.date[i][1] - 1]
            self.date[i][1] += 1
        if self.date[i][1] > 12:
            self.date[i][1] = 1
            self.date[i][2] += 1
    self.select_etudiant()

def moins(self):
    for i in [0,1]:
        self.date[i][0] -= 7
        if self.date[i][0] < 1:
            self.date[i][1] -= 1
            if self.date[i][1] >= 1:
                self.date[i][0] += mois[(self.date[i][1]) - 1]
        if self.date[i][1] < 1:
            self.date[i][1] = 12
            self.date[i][2] -= 1
            self.date[i][0] += 31
    self.select_etudiant()

def plus_day(date):
    date[0] += 1
    if date[0] > mois[date[1] - 1]:
        date[0] -= mois[date[1] - 1]
        date[1] += 1
    if date[1] > 12:
        date[1] = 1
        date[2] += 1
    return date

def moins_day(date):
    date[0] -= 1
    if date[0] < 1:
        date[1] -= 1
        if date[1] >= 1:
            date[0] += mois[(date[1]) - 1]
    if date[1] < 1:
        date[1] = 12
        date[2] -= 1
        date[0] += 31
    return date