L = [3, 5, 4] ; L = L.sort()

#niepoprawne jest przypisanie L = L.sort() poniewaz L.sort() modyfikuje L ale nie zwraca niczego
# wiec przypisujemy L nic

#-----------------------

#x, y = 1, 2, 3

#niepoprawny bo jest wiecej wartosci niz zmiennych

#-----------------------

#X = 1, 2, 3 ; X[1] = 4

# X jest krotka, a w nich nie mozna zmieniac wartosci

#-----------------------

#X = [1, 2, 3] ; X[3] = 4

#indeks 3 nie istnieje

#-----------------------

#X = "abc" ; X.append("d")

# X jest stringiem, a dla stringow nie ma funkcji append

#-----------------------

#L = list(map(pow, range(8)))

#funkcja pow wymaga co najmniej 2 argumentow