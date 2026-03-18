#zadam cislo a vypocita se mi jeho faktorial

cis = input("Zadej cislo: ")

cislo = int(cis)

fakt = 1

if (cislo < 0):
    print("Faktorial nelze vypocitat pro zaporna cisla!!")
    print("Udelej si to peekne znovu :/")
elif (cislo == 0):
    print("Faktorial pro 0 je 1!")
else:
    for i in range(1, cislo + 1):
        fakt *= i
    print("Faktorial cisla", cislo, "je", fakt)


