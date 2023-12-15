#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Joc dels gigants i els talaiots
import random
import time

# Función donde explicamos qué pasa
def intro():
    print("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar,
    Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.
    Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran
    i en l'altre són uns caníbals afamats, i ens menjaràn just ens vegin.
    """)

# Función donde preguntamos a qué talaiot queremos ir
def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

# Función que nos indica si comparten la comida o seremos nosotros su bocado
def trobada(talaiot_elegit, punts):
    print("T'estas apropant al talaiot...")
    time.sleep(2)
    print("Està fosc i és tenebrós...")
    time.sleep(2)
    print("Un gran gegant salta davant teu, t'agafa i ...")
    print("")

    gegant_amic = random.choice(["1", "2"])
    if talaiot_elegit == gegant_amic:
        punts += 1
        print(f"Et convida a menjar...\nTens {punts} punts")
    else:
        print("Se't menja d'un mos... ÑAMÑAMÑAM\nTens {punts} punts")
        punts -= 1

# Función principal 
punts = 0
partida_nova = "si"
while partida_nova.lower() in ["s", "si"]:
    intro()
    n_talaiot = canviTalaiot()
    trobada(n_talaiot, punts)
    partida_nova = input("Vols tornar a mejar (jugar)? Introdueixi si o no: ")
    print("\n")

