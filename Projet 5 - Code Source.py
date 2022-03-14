#Debut
print("___________________________ PROJET # 5 ; GROUPE #5 ___________________________")
print("\nBonjour! Ce programme vous permet de calculer A à la puissance N comme :(A^N)\n\n")
print("                          ◄ ▪ ▪ ▪ D E B U T ▪ ▪ ▪ ►")
#Une boucle while pour peremetre d'utilisateur le programme plusieurs fois
test="r"
while test=="r" or test=="R":
#D'abord on saisi les valeurs:
    A=input("\nSAISIR LA VALEUR A : ")
    #Pour s'assurer que A soit toujour un réel
    TestFloat=True
    while TestFloat==True: 
        try: 
            A=float(A)
            break
        except:
            A=input("=== A doit être un nombre réel !! veillez résaisir A : ")
    #----------------------------------------------------------------------#
    N=input("SAISIR LA VALEUR N : ")
    #Pour s'assurer que N soit toujour un entier positif
    while N.isdigit()==False:
        N=input("=== N doit être un entier positif !!veillez résaisir N : ")
    N=int(N)
    #----------------------------------------------------------------------#
#Puis on définie la fonction:
    def puissance(A,N):
        if N==0: return 1
        elif N%2==0: return puissance(A,N/2)*puissance(A,N/2)
        else: return A*puissance(A,N-1)
#Enfin on l'applique sur les paramétres saisis:
    print("\n▪▪▪▪▪ ► LE RESULTAT DE ",A,"^",N," EST : [",puissance(A,N),"]")
    test=input("\nSaisir r ou R pour continuer ou une autre touche pour quitter : ")
print("\n\n                            ◄ ▪ ▪ ▪ F I N ▪ ▪ ▪ ►")
print("______________________________________________________________________________")
    
#Fin
import os
os.system("pause")

