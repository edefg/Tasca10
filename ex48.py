from random import sample

def llista_20_elements():
    return sample(range(1, 101), 20)

def hi_ha_duplicats(a):
    seen = set()
    dupes = set(x for x in a if x in seen or seen.add(x))

    if dupes:
        print("La llista té elements duplicats: {}".format(list(dupes)))
    else:
        print("La llista no té elements duplicats.")

# Programa principal
x = llista_20_elements()
hi_ha_duplicats(x)

