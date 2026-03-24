#pres funkce udelam kalkulacku, zadam dve cisla

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

print("scitani:", scitani(cis1, cis2))
print("odcitani: ", odcitani(cis1, cis2))
print("nasobeni: ", nasobeni(cis1, cis2))
print("deleni: ", deleni(cis1, cis2))

