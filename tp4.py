'''
print("########### Quetion 1 ##########")
n = int(input("Entrer un Entier S'il vous plait : "))

def sommeValues(n):
    if n > 0 :
        somme = 0
        for i in range(n) :
            value = input("Entrer un entier dans la list pour fair l'addition : ")
            somme = somme + int(value)
        print(somme)
    elif n == -1 :
        k = 0
        somme = 0
        i = input("Entrer un valeur s'il vous plait : ")
        while True:
            if i != "f" :
                somme = somme + int(i)
                i = input("Entrer un valeur s'il vous plait : ")
            else :
                print(somme)
                break
 
                
sommeValues(n)
'''
'''
print("########### Quetion 3 ##########")
a = int(input("Entrer un premier paramétre : "))
b = int(input("Entrer un premier paramétre : "))
c = int(input("Entrer un premier paramétre : "))
def deux_egaux(a,b,c):
    if a == b:
        return True
    elif a ==c:
        return True
    elif b == c:
        return True
    else :
        return False
def programmeQ3(a,b,c):
    resultat = deux_egaux(a,b,c)
    print(resultat)
programmeQ3(a,b,c)
'''
print("########### Quetion 4 ##########")
h_lever = int(input("Entrer  le moment ou la solei se lever : "))
h_coucher = int(input("Entrer le moment ou la solei se coucher : "))
h_actuelle = int(input("Entrer l'etat actuelle de la solei  : "))
def inDay(a):
    if a > 0 or a < 23:
        return True
    else :
        return False
    
def solei_leve(h_lever,h_coucher,h_actuelle):
    if inDay(h_lever) and inDay(h_coucher) and inDay(h_actuelle):
        if h_actuelle > h_coucher or h_actuelle < h_lever:
            return False
        elif h_actuelle < h_coucher and h_actuelle > h_lever:
            return True
        else :
            print("Erreur de saisir ! ")
resultat = solei_leve(h_lever,h_coucher,h_actuelle)
print(resultat)
        
    








    
            
