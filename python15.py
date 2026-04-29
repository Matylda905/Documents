#zadam jedno cele cislo, pokud bude kladne, zjisti jestli je sude/liche, povazuji ho dale za delku strany ctverce a vypocitam obvod/obsah, pokud bude zaporne, zmeni ho na kladne a budu ho povazovat za hodnotu v metrech a prevedu ji na milimetry a vypisu ve tvaru x metru = y milimetru, pro nulu se vypise Zadana nula, s ni nepocitam

cislo = int(input("Zadej jedno cele cislo: "))

if cislo > 0:
    print(f"Zadane cislo je kladne: {cislo}.")
    if cislo % 2 == 0:
        print("Zadane cislo je sude.")
    else:
        print("Zadane cislo je liche.")

    obvod = cislo * 4
    obsah = cislo ** 2

    print(f"Obvod ctverce se stranou {cislo} je {obvod}.") 
    print(f"Obsah ctverce se stranou {cislo} je {obsah}.")

elif cislo < 0:
    print(f"Zadane cislo je zaporne: {cislo}.")
    kladne_cislo = abs(cislo)
    milimetry = kladne_cislo * 1000
    print(f"{kladne_cislo} metru = {milimetry} milimetru.")
else:
    print("Zadana nula, s ni nepocitam.")


