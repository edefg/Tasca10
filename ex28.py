def bintodec(bin):
    return int(bin, 2)

def llbintodec(llbin):
    lldec = [bintodec(e) for e in llbin]
    return lldec

# Programa principal
a = ["111", "11", "1010", "1000"]
b = llbintodec(a)

for i, e in enumerate(b):
    print(f"El número binari: {a[i]} correspon amb el número decimal: {e}")