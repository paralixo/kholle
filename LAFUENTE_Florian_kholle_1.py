#!/usr/bin/env python3
import sys
import csv
import re

filename = 'entiers.csv'

# Retourne tout les nombres du tableau (que les nombres soient en colonne ou en colonne)
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
    sys.argv.append('--help')
option = sys.argv[1]

# Affiche le contenu du fichier .cvs
if option == '-l':
    numbers = getAllNumbers(filename)
    print('Nombres entiers du fichier : ' + str(numbers))

# Ajoute des entiers dans le fichier .cvs
elif option == '-a':
    numbers = []
    for arg in sys.argv[2:]:
        if re.match(r"([0-9])", arg):
            numbers.append(int(arg))
        else:
            print('L\'argument "' + arg + '" n\'est pas un entier et ne sera pas pris en compte dans cette commande')

    if len(numbers) < 1:
        print('Pas d\'entier à ajouter au fichier') #####
        exit()
    
    numbers = getAllNumbers(filename) + numbers
    write(filename, numbers)

    print('Réussite de l\'écriture')

# Clear le fichier .cvs
elif option == '-c':
    write(filename, '')
    print('Clear réussi')

# Donne le plus petit/grand entier ou calcule la moyenne/somme des entiers (selon les arguments)
elif option == '-s':
    numbers = getAllNumbers(filename)
    if len(numbers) < 1:
        print('Pas d\'entiers dans le fichier')
        exit()

    if len(sys.argv) < 3:
        print('Pas assez d\'arguments') #####
        exit()

    arg = sys.argv[2]
    if arg == '--moy' or arg == '--sum':
        sum = 0
        for number in numbers:
            sum += number

        if arg == '--moy':
            moy = sum / len(numbers)
            print('La moyenne est de : ' + str(moy))
            exit()

        print('La somme est de : ' + str(sum))

    elif arg == '--min' or arg == '--max':
        rslt = numbers[0]
        for number in numbers:
            condition = rslt > number if arg == '--min' else rslt < number
            if condition:
                rslt = number
        msg = 'Le plus petit ' if arg == '--min' else 'Le plus grand '
        print(msg + 'nombre est : ' + str(rslt))

    else:
        print('Argument "' + arg + '" non valide.') ####

elif option == '-t':
    numbers = getAllNumbers(filename)
    if len(numbers) < 1:
        print('Pas d\'entiers dans le fichier')
        exit()
    
    option = 'asc'
    if len(sys.argv) > 2:
        if sys.argv[2] == '--desc':
            option = 'desc'

    rslt = []
    

else:
    option = '--help'

if option == '--help':
    print('\nAide de la commande: ')
    print('     -l, Affiche le contenu de la liste')
    print('     -a [nb1 nb2 nb3 ...], Ajoute tout les nombres données en arguments à la liste')
    print('     -c, Supprime tout les éléments de la liste')
    print('     -s --min, Affiche la plus petite valeur de la liste')
    print('     -s --max, Affiche la plus grande valeur de la liste')
    print('     -s --moy, Affiche la moyenne des valeurs de la liste')
    print('     -s --sum, Affiche la somme des valeurs de la liste')
    print('     -t, Trie les éléments de la liste dans l\'ordre croissant')
    print('     -t --desc, Trie les éléments de la liste dans l\'ordre décroissant')