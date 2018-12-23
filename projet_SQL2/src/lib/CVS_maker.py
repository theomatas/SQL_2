import csv
import lib.simple_fonction as X



def main(name,text):    
    filename = X.adresse()+ "/../planning" + name  + ".csv"
    with open(filename, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Name', 'Profession'])
        filewriter.writerow(['Derek', 'Software Developer'])
        filewriter.writerow(['Steve', 'Software Developer'])
        filewriter.writerow(['Paul', 'Manager'])