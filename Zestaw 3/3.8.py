a = input("Podaj pierwsza sekwencje: ")
b = input("Podaj druga sekwencje: ")

wspolne = list(set(a) & set(b))
wszystkie = list(set(a) | set(b))

print("Elementy wspolne:", wspolne)
print("Wszystkie elementy:", wszystkie)
