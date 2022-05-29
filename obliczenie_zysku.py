#print("obliczenie_potencjalnego_zysku")

#kwotaWkladu = int(input("Podaj kwote wkladu: "))
#oprocentowanie = int(input("Podaj oprocentowanie wkladu: "))

def obliczZysk(kwotaWkladu, procenty):
    k = procenty / 100
    zysk = kwotaWkladu * k

    return zysk
#print("Twoj zysk za rok to: ", obliczZysk(kwotaWkladu, oprocentowanie))
