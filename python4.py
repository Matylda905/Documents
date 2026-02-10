## vetsi nez 87cm, nad 12 let (+50kc),nad 18 let (+100kc),nad 65 let (+150kc), foto (40kc)
## vyska, vek, foto

minvys = 87
vys = 0

vek = 0
vek1 = 12
vek2 = 18
vek3 = 65





vyska = int(input("Zadejte výšku (cm): "))

if minvys <= vyska:
    print("Vstup povolen")
else:
    print("Vstup zakázán")
    print("Just don't be VÍTEK")
    exit (0)

cena = 0

vek = int(input("Zadejte věk: "))
foto = input("Máte fotku? (ano/ne): ")



if (vek <= vek1):
    print("+ 50 Kč")
    cena +=50

if ((vek > 13 )and(vek <= vek2)):
    print("+ 100 Kč")
    cena +=100

if (vek > 19):
    print("+ 150 Kč")
    cena +=150

if ((foto == "ano") or (foto == "Ano") or (foto == "ANO")):
    print("+ 40 Kč")
    cena +=40


print("Cena vstupenky: ", cena, "Kč")
print("Cena vstupenky: ", cena, "Kč")
print("Dělej, zaplať to!!!!!!")
print(":D")


exit (0)