#udelam kamen,nuzky, papir, uzivatel zada  cislo dle legendy, a druhy bude random vybran z knihovny random, a porovnam kdo vyhral, hraje se na 3 vitezne, kdo ziska 3 body vyhral a program konci

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

uz = 0
bot_score = 0

while uz < 3 and bot_score < 3:
    uzivatel = int(input("Zadej cislo: "))
    print("")
    if uzivatel < 1 or uzivatel > 3:
        print("Neplatný vstup, zadej číslo mezi 1 a 3.")
        continue

    if uzivatel == 1:
        print("Ty: KAMEN")
    elif uzivatel == 2:
        print("Ty: NUZKY")
    elif uzivatel == 3:
        print("Ty: PAPIR")

    bot = random.randint(1, 3)

    if bot == 1:
        print("Pan Brunclík: KAMEN")
    elif bot == 2:
        print("Pan Brunclík: NUZKY")
    elif bot == 3:
        print("Pan Brunclík: PAPIR")

    print("")

    if uzivatel == bot:
        print("Remiza!!")
        print("SKORE: Ty -", uz, "Pan Brunclík -", bot_score)
        print("")
    elif (uzivatel == 1 and bot == 2) or (uzivatel ==2 and bot == 3) or (uzivatel == 3 and bot == 1):
        uz += 1
        print("Porazil jsi Brunclu!!")
        print("Gratuluju!")
        print("SKORE: Ty -", uz, "Pan Brunclík -", bot_score)
        print("")
    else:
        bot_score += 1
        print("Pan Brunclík vyhrál!!")
        print("SKORE: Ty -", uz, "Pan Brunclík -", bot_score)
        print("")


if uz == 3:
    print("Vyhrál jsi!!")
    print("")
elif bot_score == 3:
    print("Pan Brunclík vyhrál!!")
    print("")