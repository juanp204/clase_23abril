while True:
    palabra = input("palabra = ")
    if palabra == "salir":
        print("cerrando...")
        break
    elif " " in palabra:
        print("sin espacios, solo es una palabra")
        continue
    repalabra = list(palabra).reverse()
    print(repalabra)#profeeeeeeeeeeeeeeeeeeee nose por que no me sirve esta verga ya estoy mamado de que las mierdas que hago no me sirvan,la madreeeeeeeeeee
    if list(palabra) == repalabra:
        print("es un palindromo")
    else:
        print("no es un palindromo")



