#udelam kamen,nuzky, papir, uzivatel zada  cislo dle legendy, a druhy bude random vybran z knihovny random, a porovnam kdo vyhral

import random

print("-----------------------------")
print("KAMEN, NUZKY, PAPIR")
print("-----------------------------")
print("Vyber: ")
print("--------------")
print("1 = Kamen")
print("2 = Nuzky")
print("3 = Papir")
print("--------------")

uz = int(input("Zadej cislo: "))
print("")

if uz == 1:
    print("Ty: KAMEN")
elif uz == 2:
    print("Ty: NUZKY")
elif uz == 3:
    print("Ty: PAPIR")

bot = random.randint(1, 3)

if bot == 1:
    print("Pan Brunclík: KAMEN")
elif bot == 2:
    print("Pan Brunclík: NUZKY")
elif bot == 3:
    print("Pan Brunclík: PAPIR")

print("")

if uz == bot:
    print("Remiza!!")
elif (uz == 1 and bot == 2) or (uz ==2 and bot == 3) or (uz == 3 and bot == 1):
    print("Porazil jsi Brunclu!!")
    print("Gratuluju!")
else:
    print("Pan Brunclík vyhrál!!")
    print("GG ALKANE")



