from obliczenie_zysku import *
from zloty_na_euro import PrzeliczWalute
from obliczenie_podatku_do_zaplaty import *

print ("teraz oblizamy zysk" )
x=obliczZysk(100,5)
print (x)
print ("teraz obliczamy wartość euro")
y=PrzeliczWalute(12)
print (y)
print ("teraz obliczamy podatek od zapłaty")
z=obliczPodatek(200,4)
print(z)
#print ("twoj wkład własny "+kwotaWkladu)
#print ("twoj zysk to"+oprocentowanie)
#print(" twoja kwota w euro to "+int(PrzeliczWalute))