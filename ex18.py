def invertir(a):
    return a[::-1]

# Programa principal
s = input("Introdueix una frase a invertir: ")
print("La inversa de {} és {}".format(s, invertir(s)))