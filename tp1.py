# 1
# l'installation de la language de programmation python et l'environement de travaille IDE  pycharm

# 2
y = 47
x = 2.5487

produit = 23 * 74

Division_entiere = 50 / 8

Exposant = 20**20

text = "Bienvenue"

# 3
rayon = float(input("Donnez la rayon du cercle s'il vous plait"))
diamaitre = 2 * rayon
pi = 3.14
circulation = float(diamaitre * pi)
aire = pi * rayon**2

print ("la circulation de cercle c'est =", circulation , "est l'aire =",aire)

 # 4
premiere = float(input("la premiere reel: "))
deusieme = float(input("la deusieme reel: "))
troisieme = float(input("la troisieme reel: "))
quaterieme = float(input("la quaterieme reel: "))
sinquieme = float(input("la sinquieme reel: "))

somme = premiere + deusieme + troisieme + quaterieme + sinquieme
moyen = somme / 5

print ("la Moyen est egal a :", moyen)

# 5
X = float(input("donner la valeur de X: "))
Y = float(input("donner la valeur de Y: "))
Z = float(input("donner la valeur de Z: "))

W = (Y * Z) / X

print("X/Y = Z/W  \n => W = (Y * Z) / X \n => W = (",Y ,"*", Z,") / ",X," \n =>  W = ",W )

# 6

positivea = int(input("siasir l'entier a:"))
while positivea < 0 :
    print ("saisir un nomber positive pour a :")
    positivea = int(input("siasir l'entier a:"))
a = positivea
positiveb = int(input("siasir l'entier b:"))
while positiveb < 0 :
    print ("saisir un nomber positive pour a :")
    positiveb = int(input("siasir l'entier b:"))
b = positiveb
c = float(input("siasir la reel c :"))
d = float(input("siasir la reel d :"))

print("a-b =",a-b,";")
print("b+c =",b+c,";")
print("c+d =",c+d,";")
print("a * c =",a * c ,";")
print("a/2 =",a/2,";")
print("a/(b+4) =",a/(b+4),";")
z = int(input("siasir un Entier Z:"))
print("(a+b) * z/(2b) =",(a+b) * z/(2*b),";")
print("a**(-1/2) =",a**(-1/2),";")

# 7

ch1 = str(input("Entrer un text s1 : "))
while len(ch1) < 5 :
    print("siasir un text de longueur superier a 5")
    ch1 = str(input("Entrer un text s1 : "))
s1 = ch1
ch2 = str(input("Entrer un text s2 : "))
while len(ch1) < 5 :
    print("siasir un text de longueur superier a 5")
    ch2 = str(input("Entrer un text s2 : "))
s2 = ch2

concatenation = s1 + s2
print("les caracters d'indice 1,2,3 de la text: ",s1,"sont :\n","indice 1: ",s1[1],"\nindice 2: ",s1[2],"\nindice 5: ",s1[5])
print("les caracters d'indice 1,2,3 de la text: ",s2,"sont :\n","indice 1: ",s2[1],"\nindice 2: ",s2[2],"\nindice 5: ",s2[5])
print("la concatation de "+ s1 +" est "+s2+" c'est : " +concatenation)

# 8
list = []
i = 0
k = 1
n = int(input("Entrer la taille de votre tableau s'il vous plait : "))
print("donner les elements de votre tableau : ")
while i < n :
    list.append(int(input("Entrer un Entier s'il vous plait :")))
    i = i + 1

for j in list :
    k *= j

print("la multiplication de ton list est :",k)

# 9
n = int(input("siasir un entier s'il vous plait : "))
i = 0
print("la table de multiplication de ",n ,"c'est ")
while i < 11:
    print(n,"*",i ," = ", n * i)
    i = i + 1

# 10
m = [1,3,5,7,9,11,13,15,17,19]
M = 1
for i in m :
    M = M * i
print(M)
