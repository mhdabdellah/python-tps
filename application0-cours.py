print("######################1#####################")
n = int(input("Entrer un Entier : "))
def fib(n):
    x , y = 0 , 1
    for k in range(n):
        x , y = x + y, x
        #print(y)
        #print(x)
    return x
print(fib(n))


