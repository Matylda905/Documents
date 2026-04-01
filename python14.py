#vytvorim seznam se 7 cisly

seznam1 = [1, 2, 3, 4, 5, 6, 7]

print("")
print("Původní seznam:")
print("---------------")
print(seznam1)
print("")

#vypisu cislo 3 z druheho indexu

seznam2 = [4,8,3,7,5,1,9]

print("")
print("Číslo z druhého indexu:")
print(seznam2[2])
print("")

#nastaveni hodnoty na 1,2,3,4 a 5

seznam3 = [1, 2, 3, 4, 5, 6, 7]

print("")
print("Vypis celeho seznamu: ")
seznam3 = list(range(1, 6))
print(seznam3)
print("")

#nastaveni seznamu od 0 do 5, definice cyklu, vypis hodnot seznamu 0,1,2,3,4,5

seznam4 = [5,4,6,2,1,3,0]

print("")
print("Vypis seznamu (vseho): ")
seznam4 = list(range(1,6))
for i in seznam4:
    print(i, end=" ")

#zadavam cisla do seznamu, ukoncuju nulou a vypisou se vsechny

seznam5 = []

print("")
print("Zadej čísla do seznamu (0=KONEC):")
while True:
    cislo = int(input("Zadej číslo: "))
    if cislo == 0:
        break
    seznam5.append(cislo)

print("")
print("Zadaná čísla:")
for i in seznam5:
    print(i, end=" ")

#zadam do seznamu hodnoty a zjistim nejvyssi a nejnizsi hodnotu (bez min a max), pak vypisu jejich rozdil

seznam6 = []

print("")
print("ZADANI CISLA A JEJICH ROZDIL:")
print("Zadej čísla do seznamu (0=KONEC):")
while True:
    cislo = int(input("Zadej číslo: "))
    if cislo == 0:
        break
    seznam5.append(cislo)
print("")
print("Zadaná čísla:")
print(seznam5)

nejvyssi = seznam5[0]
nejnizsi = seznam5[0]

for i in seznam5:
    if i > nejvyssi:
        nejvyssi = i
    if i < nejnizsi:
        nejnizsi = i

print("")
print("Nejvyssi hodnota: ",nejvyssi)
print("Nejnizsi hodnota: ",nejnizsi)
print("")
print("Rozdil je: ",nejvyssi - nejnizsi)
print("")

#zadavam cisla a delim je 10, ty ktere jsou delitelne, necham, ty ktere nejsou tak je vypisu zvlast

seznam7 = []

print("")
print("ZADANI CISLA A JEJICH DELENI 50:")
print("Zadej čísla do seznamu (0=KONEC):")
while True:
    cislo = int(input("Zadej číslo: "))
    if cislo == 0:
        break
    seznam7.append(cislo)
print("")
print("Zadaná čísla:")
print(seznam7)

delitelne = []
nedeletelne = []

for i in seznam7:
    if i % 10 == 0:
        delitelne.append(i)
    else:
        nedeletelne.append(i)

print("")
print("Čísla dělitelná 50:")
print("")
for i in delitelne:
    print(i, end=" ")
    
print("")
print("Čísla nedělitelná 50:")
print("")
for i in nedeletelne:
    print(i, end=" ")

print("")
for i in nedeletelne:
    if i % 5 == 0:
        
        print(i, "je delitelne 5")


