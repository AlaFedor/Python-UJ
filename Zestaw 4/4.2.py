def make_ruler(n):
    dlugosc = n
    miarka = "|"
    liczby = "0"

    for i in range(dlugosc):
        miarka +="....|"
        odstęp = 5 - len(str(i+1))
        liczby += " " * odstęp + str(i+1)

    calosc = miarka +'\n'+ liczby

    return calosc

def make_grid(rows, cols):
    wysokosc = rows
    dlugosc = cols

    poziome = '+'
    pionowe = '|'

    for i in range(dlugosc):
        poziome+='---+'
        pionowe+='   |'

    calosc = poziome
    for i in range(wysokosc):
        calosc+= '\n' + pionowe + '\n' + poziome 

    return calosc

print(make_ruler(10))
print(make_grid(2,4))
