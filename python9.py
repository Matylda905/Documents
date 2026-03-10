#zadam heslo a reknu zda je silne nebo ne, to zjistim pomoci poctu znaku, velky/maly pismena znamenka a cisla
#overuju zda obsahuje cisla, znamenka a velka/mala pismena
#vse pomoci stringu

heslo = input("Zadej heslo: ")
print("")

x = len(heslo)

for i in range(x):
    if (x < 8):
        print("Heslo je kratke!!")
        print("musi mit vic jak 8 znaku")
        print("Udelej si to hezky znovu :)")
        print("")
        break
    elif (heslo[i]>="a" and heslo[i]<="z"):
        print("Heslo musi obsahovat mala pismena!!")
        print("Udelej si to hezky znovu :)")
        print("")
        
    
    elif (heslo[i]>="A" and heslo[i]<="Z"):
        print("Heslo musi obsahovat velka pismena!!")
        print("Udelej si to hezky znovu :)")
        print("")
        
    elif (heslo[i]>="0" and heslo[i]<="9"):
        print("Heslo musi obsahovat cisla!!")
        print("Udelej si to hezky znovu :)")
        print("")
        
    elif (heslo[i]>="!" and heslo[i]<="/"):
        print("Heslo musi obsahovat znamenka!!")
        print("Udelej si to hezky znovu :)")
        print("")  
        
    else: 
        print("Heslo je silne!!")
        print("Gratuluji :)")




