#babcika ma doma k kraliku a s slepic, napisu program, ktery vytiskne jak celkovy pocet hlav, tak celkovy pocet nohou, uloha ma dve mozna reseni

kralik = int(input("Zadej pocet kraliku: "))
slepice = int(input("Zadej pocet slepic: "))

pocet_hlav = kralik + slepice
pocet_nohou = (kralik * 4) + (slepice * 2)

print(f"Celkovy pocet hlav je: {pocet_hlav}.")
print(f"Celkovy pocet nohou je: {pocet_nohou}.")
