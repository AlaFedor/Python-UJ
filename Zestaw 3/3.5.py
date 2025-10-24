dlugosc = int(input("wprowadz dlugosc"))

miarka = "|"
liczby = "0"

for i in range(dlugosc):
    miarka +="....|"
    odstęp = 5 - len(str(i+1))
    liczby += " " * odstęp + str(i+1)

calosc = miarka +'\n'+ liczby

print(calosc)

