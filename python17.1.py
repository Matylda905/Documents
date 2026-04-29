#zadam nohy a hlavy a podle toho se vypise kolik je kraliku a kolik je slepic

pocet_hlav = int(input("Zadej celkovy pocet hlav: "))
pocet_nohou = int(input("Zadej celkovy pocet nohou: "))

# Kralik = 1 hlava a 4 nohy, slepice = 1 hlava a 2 nohy

kralik = (pocet_nohou - (2 * pocet_hlav)) // 2
slepice = pocet_hlav - kralik

print(f"Celkovy pocet kraliku je: {kralik}.")
print(f"Celkovy pocet slepic je: {slepice}.")
