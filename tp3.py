import random
from math import sqrt
'''
print ("########Question 1 ############")
n = int(input("Entrer un nommber Entier : "))

def suit(n):
   prec = 0
   succ = 1
   print (prec)
   print(succ)
   for i in range(n - 2) :
        somme = prec + succ
        print (somme)
        prec = succ
        succ = somme
        
suit(n)
'''

print ("########Question 2 ############")
pli = 30
choi = int(input("Combient de plis sont-il nécessaire sur la lune ? : "))
def game(choi):
    for i in range(4):
        if choi == pli:
            print("Bravo !")
            break
        else:
            choi = int(input("Combient de plis sont-il nécessaire sur la lune ? : "))
    if pli != choi:
        print("Mouvaise réponse !")

game(choi)

print ("########Question 3 ############")
list = []
somme = 0
while True:
    number = int(input("Entrer un entier s'il vous plait : "))
    if number != -1 : 
         list.append(number)
    else :
        for i in list :
            somme = somme + i
        moyen = somme / len(list)
        print("La moyenne arithmétique calculée égale : ", moyen)
        break
   
print ("########Question ??????? ############")
n = int(input("Entrez un Entier : "))
list = []
array = []
def  TableX(n):
    for i in range(n):
        list.append("X")
    for i in range(n):
        array.append(list)
    print(array)
TableX(n)

print ("########Question 4 ############")
n = int(input(" Entrez un Entier : "))
i = 0
j = 0
list = []
while i < n:
   while j<n:
       list.append("X")
       j+=1
   print(list)
   i+=1
'''
'''
print ("########Question 5 ############")
n = int(input(" Entrez un Entier : "))
for i in reversed(range(1,n+1)):
   print(''*(n-1)+'x'*i)

print ("########Question 6 ############")
secret = random.randint(0,100)
preposition = int(input("Bienvenu Joueur Poposer un Nombre S'il Vous Plait : "))
def getSecretValue(preposition):
    for i in range(5):
        if (preposition > secret):
            print ("Trop grand ! Et Vous Reste",5-i,"chance")
            preposition = int(input("Bienvenu Joueur Poposer un Nombre S'il Vous Plait : "))
        elif (preposition < secret):
            print ("Trop petit ! Et Vous Reste",5-i,"chance")
            preposition = int(input("Bienvenu Joueur Poposer un Nombre S'il Vous Plait : "))
        else:
            print("Gagné !")
    if preposition != secret:
        print("Mouvaise Proposition tu as perdu !")
getSecretValue(preposition)


print ("########Question 7 ############")



print ("########Question 8 ############")


'''
def cher(x,l):
    i,j = 0, len(j)
    while i<j:
        k = (i +j) // 2
        if l(k) == x:
            return True
        elif l[k] > x:
            
'''















































