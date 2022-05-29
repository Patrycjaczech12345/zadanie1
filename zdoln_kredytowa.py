#print("zdolnosc_kredytowa")

#wiek = int(input("Podaj wiek"))
#plec = input("Podaj plec")

def zdolnosc_kredytowa(wiek, plec):
    if(wiek > 60 and plec == "K"):
        print("Nie masz zdolnosci kredytowej")
        return False
    if(wiek > 65 and plec == "M"):
        print("Nie masz zdolnosci kredytowej")
        return False
    print("Masz zdolnosc kredytowa")
    return True
#zdolnosc_kredytowa(wiek,plec)



