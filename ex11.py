
def menu_principal():
    print("""
        Menu principal:
          1.caculadora numeros enters
          2.calculadora numeros reals
          3.sortir
        """)
    a = int(input("Elegeix una opcio"))
    return a
def calculadora enters():
        op = 1
        while op>0:
        print("""
          1.Menu enters
          1. sumar
          2. restar
          3. dividir
          4. multiplicar 
          5. sortir
      """)
    op = int(input("Elegeix una opcio: ")
    match op:
        case 1:
            x = int(input("Introdueix el primer nombre: ")
            y = int(input("Introdueix en segon nombre: ")
            print("{} + {} = {}".Format(x,y,x+y))
        case 2:
            x = int(input("Introdueix el primer nombre: ")
            y = int(input("Introdueix en segon nombre: ")
            print("{} - {} = {}".Format(x,y,x-y))
        case 3:
            x = int(input("Introdueix el primer nombre: ")
            y = int(input("Introdueix en segon nombre: ")
            print("{} * {} = {}".Format(x,y,x*y))
        case 4:
              x = int(input("Introdueix el primer nombre: ")
            y = int(input("Introdueix en segon nombre: ")
            print("{} / {} = {}".Format(x,y,x/y))
        case 5:
            print("Adeu, ja tornaras a la calculadora inicial \n\n")
            op=-1
def calculadora_reals():
    op = 1
    while op>0:
        print("""
            Menu enters
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Sortir
        """)
        op = int(input("Elegeixi una oppcio: "))
        match op
            case 1: #Sumar
                x = float(input("Introdeuix el primer numero: "))
                y = float(input("introdueix el segon numero: "))
                print(" {} + {} = {}".format(x, y, x+y))
            case 2:#Restar
                x = float(input("Elegeix el primer nombre": ))
                y = float(input("Elegeix el segon nombre": ))
                print (" {} - {} = {}".format(x, y, x-y))
            case 3:#Multiplicar
                x = float(input("Elegeix es primer nombre: "))
                y = float(input("Elegeix el segon nombre: "))
                print(" {} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = float(input("Elegeix el primer nombre: "))
                y = float(input("Elegeix el segon nombre: "))
                print(" {} / {} = {}".format(x, y, x/y))
            case 5: #Sortir
                print("Adeu, ja tornaras a la calculadora inicial \n\n")
                op=-1
   


#funcions canvis de base 
# de decimal a binari,octal i hexadecimal
def dectobin(numero):
    return bin (numero)
def dectooct(numero):
    return oct(numero)
def dectohex hex(numero):
    return hex(numero)

def canvis_base():
op = 1
while op>0:
    print("""
        
        Menu canvia de base
        1.Donat un binari ho passam a tota la resta
        2.Donat un octal el passam a tota la resta
        3.Donat un decimal o passam a tota la resta
        4.Donat un hexadecimal ho passam a tota la resta
    """)
    op = int(input("Elegir una opcio: "))
    match op:
        case 1:
            b = input("Introdueix el numero binari")

def dectobin(numero):
    return bin (numero)
def dectooct(numero):
    return oct(numero)
def dectohex(numero):
    return hex(numero)

x = int(input("Introdueix un numero en decimal: "))
print(dectooct(x))






          

