def factorial(n):
    if n < 0:
        raise ValueError("nie mozna uzyc liczb ujemnych do obliczenia silni")

    silnia = 1
    for i in range(n):
        silnia = silnia * (i+1)

    return silnia

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))