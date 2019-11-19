def anterior_posterior():
    n= input("ponga su numero: ")
    print "los anteriores son:"
    for a in range(n-3,n):
        print a
        a= a+1
    print"los posteriores son:"
    for s in range(n+1,n+4):
        print s
        s= s+1
anterior_posterior()
