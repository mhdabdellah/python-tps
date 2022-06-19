######exo1#######

m = int(input("Entrez le nombre des lignes :"))
n = int(input("Entrez le nombre des colones :"))

def initlist(a):
    m = []
    for i in range(a):
        m.append(0)
    return m
def initmatrice(m,n):
    n = initlist(n)
    matrice =[]
    for i in range(m):
       matrice.append(n)
    return matrice

matrice = initmatrice(m,n)
print(matrice)

