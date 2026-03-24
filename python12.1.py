#pres funkce udelam kalkulacku, zadam dve cisla a pres if vyberu operaci

def scitani(a, b):
    return a + b

def odcitani(a, b):
    return a - b

def nasobeni(a, b):
    return a * b

def deleni(a, b):
    if b == 0:
        return "NEMUZES DELIT NULOU!!"
    else:
        return a / b

print("-----------------------------")
print("KALKULATOR 3000")
print("-----------------------------")

cis1 = int(input("Zadej prvni cislo: "))
cis2 = int(input("Zadej druhe cislo: "))
print("--------------")
print("Vyber operaci:")
print("--------------")
print("1 = scitani")
print("2 = odcitani")
print("3 = nasobeni")
print("4 = deleni")
print("--------------")
operace = int(input("Zadej cislo operace: "))
print("")

if operace == 1:
    print("scitani:", scitani(cis1, cis2))
elif operace == 2:
    print("odcitani: ", odcitani(cis1, cis2))
elif operace == 3:
    print("nasobeni: ", nasobeni(cis1, cis2))
elif operace == 4:
    print("deleni: ", deleni(cis1, cis2))