def canvi(l):
    #per llegir un nombre a modificar de pocicio
    x = int(input("Introdueix la pocisio a modificar: "))
    l[x]=input("introdueix el valor a inserir: ")
#programa principal
#definir una llista a una variable
a=[3, 4, 5, 6, 7, 8, 'a', (1,2),[3,4],10]
print("El valor de la lllista abans de canviar es: {}".format(a))
canvi(a)
print("El valor de la llista despres de canviarla es: {}".format(a))

def canvi(l,m,n):
    print("1) {}{} \n {}".format(l, m,n))
    l='Adeu'
    m='Fede'
    n='Que vaigi be'
    print("2) {}{} \n {}".format(l,m,n)) 
a='Hola, '
b='Ramis.'
c='Com estas?'
print("el valor de la variable abans de canviar es {}{}\n {}".format(a,b,c))
canvi(a, b, 6)
print("El valor de la variable despres de canviar es: {}{}\n {}".format(a,b,c))
