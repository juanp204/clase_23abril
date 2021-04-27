#ejercicio 1
datos = [4,5,9,10] #datos a manejar
for i in range(len(datos)): #imprime los la informacion de "datos"
    print(datos[i], end=" ")
#ejercicio2
datos[2]=-10 #cambia el dato de la pocicion 2 que es 9 a -10
for i in range(len(datos)):#imprime otravez los datos de "datos"
    print(datos[i], end=" ")
#ejercicio3
datos.insert(1, 11)#agrega en la pocicion 1 el numero 11
for i in range(len(datos)):#imprime todos los datos
    print(datos[i], end=" ")
#ejercicio4
datos.remove(5) #no es util, no sirve de nada seria mejor quitar y omitir toda esta parte
for i in range(0, len(datos)):#vuelve a imprimir datos
    print(datos[i], end=" ")
#ejercicio5
datos = datos + [21, 22] #INGRESA ALFINAL DE LA LISTA EL 21 Y 22
for i in range(0, len(datos)):#IMPRIME TODOS LOS NUMEROS OTRA VEZ
    print(datos[i], end=" ")
