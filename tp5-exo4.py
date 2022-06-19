print("##########exo4###########")
mot = str(input("Entrez le nombre des lignes :"))
def str_dect(mot):
    dictionnaire = {}
    for lement in mot.split(' '):
        dictionnaire[lement] = len(lement)
    print(dictionnaire)

str_dect(mot)
