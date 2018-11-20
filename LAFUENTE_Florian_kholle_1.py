#!/usr/bin/env python3
import sys
import csv
import re

filename = 'entiers.csv'

# Retourne tout les nombres du tableau (que les nombres soient en colonne ou en colonne)
# Note: les nombres doivent être des entiers
def getAllNumbers(filename):
    csvfile = open(filename, newline='')
    reader = csv.reader(csvfile)
    numbers = []

    for row in reader:
        for string in row:
            tempNb = ''
            i = 0
            for char in string:
                i += 1
                if re.match(r"[0-9]", char):
                    tempNb = tempNb + char
                elif len(tempNb) > 0:
                    numbers.append(int(tempNb))
                    tempNb = ''
            
                if len(tempNb) > 0 and i == len(string):
                    numbers.append(int(tempNb))
                    tempNb = ''

    csvfile.close()
    return numbers

def write(filename, writtenData):
    csvfile = open(filename, 'w', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(writtenData)
    csvfile.close()

# Si pas d'options, on choisit une option par défaut
if len(sys.argv) < 2:
    sys.argv[1] = '--help'
option = sys.argv[1]

# Affiche le contenu du fichier .cvs
if option == '-l':
    numbers = getAllNumbers(filename)
    print('Nombres entiers du fichier : ' + str(numbers))

# Ajoute des entiers dans le fichier .cvs
if option == '-a':
    numbers = []
    for arg in sys.argv[2:]:
        if re.match(r"([0-9])", arg):
            numbers.append(int(arg))
        else:
            print('L\'argument "' + arg + '" n\'est pas un entier et ne sera pas pris en compte dans cette commande')

    if len(numbers) < 1:
        print('Pas d\'entier à ajouter au fichier')
        exit()
    
    numbers = getAllNumbers(filename) + numbers
    write(filename, numbers)

    print('Réussite de l\'écriture')

# Clear le fichier .cvs
if option == '-c':
    write(filename, '')
    print('Clear réussi')
    
