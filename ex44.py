a = input("Introdueix un número: ")

# Verificar si la entrada es un número
if a.isdigit():
    suma = sum(int(digit) for digit in a)
    print("{} té {} dígits".format(a, len(a)))
    print("La suma dels dígits del número {} és {}".format(a, suma))

    if suma % 2 == 0:
        print("La suma dels dígits del número {} és parell".format(a))
    else:
        print("La suma dels dígits del número {} és senar".format(a))
else:
    print("Entrada no vàlida. Si us plau, introdueix només dígits.")

