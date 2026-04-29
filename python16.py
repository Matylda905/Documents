#vypocitej objem kuloveho zasobniku, jehoz polomer [r] je zadan v metrech. Na zaklade prirazeni vypiste, na jak dlouho vydrzi voda pro jednoho cloveka, kdyz vite, ze za den spotrebuje 5l vody
#V=4/3*3.14*r**3
#1 l = 1 dm3

import math
print("")
r = float(input("Zadej polomer kuloveho zasobniku v metrech: "))
print("")

objem = (4/3) * math.pi * r**3

print(f"Objem kuloveho zasobniku s polomerem {r} metru je {objem:.2f} litru.")
print("")

objem = objem * 1000
spotreba_na_den = 5  # litru

vydrz_vodou = objem / spotreba_na_den

print(f"Voda z kuloveho zasobniku vydrzi pro jednoho cloveka priblizne {vydrz_vodou:.2f} dni.")
print("")