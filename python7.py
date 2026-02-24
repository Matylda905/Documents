#50-100 krok 

print("")

for i in range(50, 101, 5):
    print(i, end=" ")

#100-50 krok -5

print("")

for i in range(100, 49, -5):
    print(i, end=" ")

#50-100 krok 5 pres while

print("")

i = 50
while i <= 100:
    print(i, end=" ")
    i+=5


#100-50 krok -5 pres while

print("")

i=100
while i >=50:
    print(i, end=" ")
    i-=5

#uzivatel zada od,do a krok a pokud prehodi cislo tak se stejne prehodi a bude pocitat od mensiho po vetsi

print("")

od = int(input("Zadej OD: "))
do = int(input("Zadej DO: "))

if od > do:
    od, do = do,od

krok = int(input("Zadej KROK: "))

if krok <=0:
    print("MUSÍ BÝT KLADNÉ!!!")
else: 

    for i in range(od, do +1, krok):
        print(i, end=" ")

#.

print("")

od = int(input("Zadej OD: "))
do = int(input("Zadej DO: "))
krok = int(input("Zadej KROK: "))

if krok <=0:
    print("MUSÍ BÝT KLADNÉ!!!")
else: 

    for i in range(od, do +1, krok):
        print(i, end=" ")
    
    for i in range(do, od -1, -krok):
        print(i, end=" ")


#uzivatel zada od,  do a krok a vypocita se prumer, soucet a kolik cisel bude mezi od a do

print("")

od = int(input("Zadej OD: "))
do = int(input("Zadej DO: "))
krok = int(input("Zadej KROK: "))

if krok <=0:
    print("MUSÍ BÝT KLADNÉ!!!")
else:
    sou = 0
    poc = 0

    for i in range(od, do +1, krok):
        sou += i
        poc += 1

    print("Součet: ", sou)
    print("Počet: Cisel je ", poc)
    print("Průměr: ", sou/poc)

#zadavam cisla dokud není 0 a pak se vypise prumer, soucet a kolik cisel bylo zadano

print("")

sou = 0
poc = 0

while True:
    cislo = int(input("Zadej číslo (0=KONEC): "))
    if cislo == 0:
        break
    sou += cislo
    poc += 1

if poc > 0:
    print("Součet: ", sou)
    print("Počet: Cisel je ", poc)
    print("Průměr: ", sou/poc)
else:
    print("Nic si nezadal ty pablbe :)")







