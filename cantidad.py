def cantidad():
    palabra=raw_input("introduzca su palabra: ")
    numero=input("introduzca su numero: ")
    lista={}
    for letra in palabra:
        if letra in lista:
            lista[letra]=lista[letra]+1
        else:
            lista[letra]=0
    print("%s se repite%s veces." %(letra,lista))
                      
cantidad()
