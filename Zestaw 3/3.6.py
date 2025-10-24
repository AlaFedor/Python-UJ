wysokosc = int(input("podaj wysokosc (liczbe kratek) "))
dlugosc = int(input("podaj dlugosc (liczbe kratek) "))

poziome = '+'
pionowe = '|'

for i in range(dlugosc):
    poziome+='---+'
    pionowe+='   |'

calosc = poziome
for i in range(wysokosc):
    calosc+= '\n' + pionowe + '\n' + poziome 

print(calosc)
