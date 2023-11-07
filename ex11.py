
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
    print("Hem passat per la calculadora de nombres reals")
#programa principal
a = 1
while a>0:
    a = menu_principal()
    match a:
        case 1:
            calculadora_enters()
        caase 2:
            calculadora_reals()
        case 3:
            a = -1
        case other:
            print("opcio no valida")
               
    