print("######exo2#######")
def print_mat(m):
    lign = len(m)
    trace = 0
    for i in range(lign):
        colone = len(m[i])
        for j in range(colone):
            print(m[i][j],end=' ')
        print()

M = [ [3, 1, 5], [9, 8, -1], [10, 12, 2] ]

print_mat(M)
