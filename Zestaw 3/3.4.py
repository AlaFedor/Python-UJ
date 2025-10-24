while True:
    x = input("podaj liczbe lub wpisz 'stop' aby zakonczyc ")

    if(x.lower() == "stop"): break

    try:
        liczba = float(x)
        print("x: ", liczba, "x^3: ", liczba**3)
    except ValueError:
        print("wprowadzono bledne dane, podaj liczbe lub stop")