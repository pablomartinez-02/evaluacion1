def operacion():
    a=input("introduce un numero: ")
    b=input("introduce otro numero: ")
    c=raw_input("que quieres hacer: ")
    if(c=="S"):
     print a+b
    if(c=="R"):
     print a-b
    if(c=="M"):
     print a*b
    if(c=="D"):
     print a/b
    if(a/b==0):
      print"no solucion"
operacion()
