def sumar(a, b):
    suma = 0
    for i in range(min(a, b), max(a, b) + 1):
        suma += i
    return suma

# PPrincipal
a = int(input("Introdueixi el primer número: "))
b = int(input("Introdueixi el segon número: "))
c = sumar(a, b)
print("La suma dels números entre {} i {} és {}".format(a, b, c))
