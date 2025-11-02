def flatten(sequence):
    wynik = []
    for i in sequence:
        if isinstance(i, (list, tuple)):
            wynik = wynik + flatten(i)
        else:
            wynik.append(i)
    return wynik

print(flatten([1,2,3,4]))
print(flatten([1,2,(3,4)]))
print(flatten([([1,2],3),4]))