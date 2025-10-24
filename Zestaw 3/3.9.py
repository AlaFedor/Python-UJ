sekwencja = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

wynik = []
for i in sekwencja:
    suma = sum(i)
    wynik.append(suma)

print(wynik)
