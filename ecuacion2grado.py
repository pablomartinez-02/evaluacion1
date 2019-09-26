def calcular(a, b, c):
    import math
    disc = (math.pow(b, 2)) - (4 * a * c)
    if disc > 0:
        x1 = (-b + math.sqrt(disc)) / (2 / a)
        x2 = (-b - math.sqrt(disc)) / (2 / a)
        print "\n\nLa ecacuacion tiene dos posibles soluciones: x1 = %.2f y x2 = %.2f" % (x1, x2)
    else:
        if disc == 0:
            x1 = -b / (2 * a)
            print "\n\nLa ecuacion tiene una posible solucion: x = %.2f" % (x1)
        else:
            xr = -b / (2 * a)
            xi = (math.sqrt(-disc)) / (2 * a)
            print "\n\nLa ecuacion tiene dos posibles soluciones, una real xr = %.2f y una imaginarinaria xi = %.2fi" % (xr, xi)
 
print "Solucionador de ecuaciones de segundo grado"
print "_" * 43
a = raw_input("\tEscriba el valor de a: ")
while a == 0:
    a = raw_input("\tEl valor de a no puede ser 0, por favor corrijalo: ")
b = raw_input("\tEscriba el valor de b: ")
c = raw_input("\tEscriba el valor de c: ")
 
a = float(a)
b = float(b)
c = float(c)
 
calcular(a, b, c)
