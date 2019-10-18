def primo():
    numero=input("say me your number")
    primo=True
    for i in range(1,numero):
        print i
        for  cont in range(2,i):
            if(i%cont==0):
                primo=False
        if( primo ==True):
            print "es primo"
        else:
            print "no es primo"
        primo=True
primo()

