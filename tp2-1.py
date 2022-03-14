import random
from math import sqrt
'''
secret = random.randint(0,5)
valeurChoisie = int(input("choisir un Valeur pour "))


def getSecretValue(valeurChoisie):
    if (valeurChoisie == secret):
        print ("tu as gagné !")
    else:
        print ("tu as perdu")

getSecretValue(valeurChoisie)

print ("Choisir un 3 nomber entier :")
valeur1 = int(input("choisir un premier Valeur  "))
valeur2 = int(input("choisir un  deuxiem Valeur "))
valeur3 = int(input("choisir un troisiem Valeur "))

def Comparer(valeur1,valeur2,valeur3):
    if (valeur1 == valeur2):
        print (valeur1)
    elif(valeur1 == valeur3):
        print (valeur1)
    elif(valeur3 == valeur2):
        print (valeur2)

Comparer(valeur1,valeur2,valeur3)

print ("Choisir un 3 nomber entier :")
a = int(input("choisir un premier Valeur pour a  "))
b = int(input("choisir un  deuxiem Valeur pour b"))
c = int(input("choisir un troisiem Valeur pour c"))

def operation(a,b,c):
    if (c==1):
        print ("a + b = ",a+b)
    elif(c==2):
        print ("a - b = ",a-b)
    elif(c == 3):
        print (" a * b = ",a*b)
    elif(c == 4):
        print (" a**2 + a * b = ",(a**2) + a * b)
    else :
        print("Erreur")

operation(a,b,c)


print ("Choisir un 2 nomber reel strictement positive :")
a = float(input("choisir un premier Valeur pour a  "))
b = float(input("choisir un  deuxiem Valeur pour b"))

def isPositive(a):
    if (a > 0):
        return True
    else :
        return False
    
def produit(a,b):
    return a * b

def racineCarre(a,b):
    if(isPositive(a) and isPositive(b)):
        print ("la racine carre du produit de a par b egale : ", sqrt(produit(a,b)))
    else :
        print("Erreur")
        
racineCarre(a,b)

list = ["T","C","O","D","I"]
var = input(" Entrer la premier Lettre de votre Polyedre : ")
a = float(input("Donner son cotté : "))
def volumePolyedre(var,list,a) :
    if var in list:
        if var == "T":
            print ("Nom : Tétraédre est son Volume = ", (sqrt(2)/12) * a**3)
        elif var == "C":
            print ("Nom : Cube est son Volume = " ,a**3)
        elif var == "O":
            print ("Nom : Octaédre est son Volume = " ,(sqrt(2)/3) * a**3)
        elif var == "D":
            print ("Nom : Dodécaédre est son Volume = " ,(15 + 7 * sqrt(2)/4) * a**3)
        elif var == "I":
            print ("Nom : Icosaédre est son Volume = " ,(5 + (3 + sqrt(5))/4) * a**3)
        else :
            print("Polyédre non connu")

volumePolyedre(var,list,a)
'''

            
        
        
    



























