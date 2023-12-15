from random import randint

def llista_20_elements():
    return [randint(1, 100) for _ in range(20)]

def hi_ha_duplicats(a):
    seen = set()
    dupes = [x for x in a if x in seen or seen.add(x)]
    
    if dupes:
        print("La llista {} té elements duplicats: {}".format(a, dupes))
    else:
        print("La llista {} no té elements duplicats.".format(a))

def elimina_duplicats(a):
    b = list(set(a))
    b.sort()
    return b

# Programa principal
x = llista_20_elements()
hi_ha_duplicats(x)
y = elimina_duplicats(x)
print("Llavors, la llista sense elements duplicats és {}".format(y))