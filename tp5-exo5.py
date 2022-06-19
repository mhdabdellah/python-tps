def calcul_prix(produit,catalogue):
    for clet in produit.keys():
        if  clet in catalogue.keys():
            resultat += produit[clet] * catalogue[clet]

    return resultat
