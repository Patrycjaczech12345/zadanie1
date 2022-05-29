from stan_zdrowia import *
nalogi = input("Wpisz t lub n")
choroby = input("Wpisz t lub n")
operacje = input("Wpisz t lub n")

x = stan_zdrowia(nalogi, choroby, operacje)
print(x)