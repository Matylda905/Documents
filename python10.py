#zadam slovo a zjistim zda je palindrom

sl = input("Zadej slovo: ")

pali = sl[::-1]

if (sl == pali):
    print("Slovo je palindrom!!")
    print("Gratuluji ;) ")
else:
    print("Slovo neni palindrom!!")
    print("Udelej si to peekne znovu :/")


