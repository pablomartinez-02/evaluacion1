def primo():
    numero=input("say me your number")
    primo=True
    for i in range(2,numero):
     if (numero % i==0):
         primo= False
    if(primo==True):
     print "es primo"
    else:
        print "no es primo"
primo()

