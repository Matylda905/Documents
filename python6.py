#program ktery necha uzivatele hadat cislo mezi 1 a 10, dokud neuhadne spravne

import random

cislo = random.randint(1, 10)
pokusy=0

while (True):
    print("Hádej číslo mezi 1-9")

    tip =int(input("Tip: "))
    

    if(tip < cislo):
        print("Číslo je větší")
        pokusy+=1
    elif (tip > cislo):
        print("Číslo je menší")
        pokusy+=1
    elif (tip == cislo):
        print("BBBBINGOOO")
        print("Uhádl jsi číslo: ", cislo)
        print("Počet pokusů: ", pokusy)
        break


