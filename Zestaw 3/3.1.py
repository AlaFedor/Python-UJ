x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

#nie jest poprawny skladniowo poniewaz w Python nie dodajemy srednikow na koncu wyrazen

#---------------------------

#for i in "axby": if ord(i) < 100: print (i)

#nie jest poprawny poniewaz po dwukropku moze wystapic tylko jedna prosta instrukcja w jednej linii,
# trzeba uzyc separatora, np:

for i in "axby":
     if ord(i) < 100: print (i)

# ---------------------------

for i in "axby": print (ord(i) if ord(i) < 100 else i)

#to jest poprawne bo po ':' ma tylko jedna instrukcje