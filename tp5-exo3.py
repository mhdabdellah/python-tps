print("############exo3###########")
def trace(m):
    lign = len(m)
    trace = 0
    for i in range(lign):
        colone = len(m[i])
        for j in range(colone):
            if i == j:
                trace += m[i][j]
    return trace
M = [ [3, 1, 5], [9, 8, -1], [10, 12, 2] ]
resultat = trace(M)
print("la trace c'est = ",resultat)
