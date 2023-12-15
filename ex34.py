def any_traspas(any):
    if (any % 4 == 0) and (any % 100 > 0 or any % 400 == 0):
        print("'L'any {any} és de traspàs")
    else:
        print("'L'any {any} no és de traspàs")

# Programa principal
a = int(input("Indiqui un any amb 4 xifres (aaaa): "))
any_traspas(a)

