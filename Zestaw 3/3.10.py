#bezposredni zapis klucz:wartosc
slownik = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

#uzywajac dict
slownik = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

#dodajac po kolei wartosci do pustego slownika
slownik = {}
slownik['M'] = 1000
slownik['D'] = 500
slownik['C'] = 100
slownik['L'] = 50
slownik['X'] = 10
slownik['V'] = 5
slownik['I'] = 1

def rzymska_na_arabska(liczba_rzymska):
    wynik = 0
    poprzednia = 0
    for znak in reversed(liczba_rzymska.upper()):
        wartosc = slownik[znak]
        if wartosc >= poprzednia:
            wynik += wartosc
        else:
            wynik -= wartosc
        poprzednia = wartosc
    return wynik

rzymska = input("Wprowadz liczbe rzymska: ")
arabska = rzymska_na_arabska(rzymska)
print("Liczba arabska: ", arabska)