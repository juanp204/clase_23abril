print("deje en blanco para dejar de ingresar nombres")
B = []
C = []
while True:
    A = input("ingrese nombres ")
    if bool(A) == False:
        break
    B.append(A)
    C.append(len(A))

for x in range(len(B)):
    print(B[x], end="-{} ".format(C[x]))