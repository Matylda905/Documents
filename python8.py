# kalkulator

x = float(input("Zadej první číslo: "))
print("")
y = float(input("Zadej druhé číslo: "))
print("")

print("------------------------------")
print("1 - +, 2 - -, 3 - *, 4 - /")
print("------------------------------")
print("")

op = input("Zadej znaménko: ")
print("")


if op == 1:
    print("Výsledek je: ", x + y)
    print("")
    print(f"{x} + {y} = {x + y}")
elif op == 2:
    print("Výsledek je: ", x - y)
    print("")
    print(f"{x} - {y} = {x - y}")
elif op == 3:
    print("Výsledek je: ", x * y)
    print("")
    print(f"{x} * {y} = {x * y}")
elif op == 4:
    if y == 0:
        print("Nulou ne!!")
    else:
        print("Výsledek je: ", x / y)
        print("")
        print(f"{x} / {y} = {x / y}")
else:
    print("Neplatný znak!!")
    print("udelej si to hezky znovu :)")

print("")
