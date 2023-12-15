import random

def generar_codi():
    return "".join(map(str, random.sample(range(0, 9), 4)))

def jugar_mastermind():
    codi = generar_codi()
    print("""Això és el teu primer Mastermind.
    Has d'adivinar un número de 4 xifres diferents.
    """)
    
    intents = 0
    while True:
        lateva_proposta = input("Introduexi un codi de 4 xifres: ")
        
        if lateva_proposta == codi:
            intents += 1
            print(f"Felicitats! Has endevinat el codi en {intents} intents.")
            break
        
        encerts = sum(1 for i, x in enumerate(lateva_proposta) if x == codi[i])
        coincidencies = sum(1 for x in set(lateva_proposta) if x in codi)
        
        print(f"La teva proposta ({lateva_proposta}) té {encerts} encerts i {coincidencies} coincidències.")
        
        intents += 1