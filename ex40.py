a = input("Introdueix un número: ")

# Verificar si la entrada es un número
if a.isdigit():
    print("{} té {} dígits".format(a, len(a)))
else:
    print("Entrada no vàlida. Si us plau, introdueix només dígits.")

