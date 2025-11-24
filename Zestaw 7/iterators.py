import random

def function_a():
    x = 0
    while True:
        yield x % 2
        x +=1

def function_b():
    choice = ("N", "E", "S", "W")
    while True:
        yield random.choice(choice)


def function_c():
    i = 0
    while True:
        yield i
        i = (i + 1) % 7


if __name__ == "__main__":
    it = function_a()
    for i in range(5):
        print(next(it))

    it2 = function_b()
    for i in range(5):
        print(next(it2))


    it3 = function_c()
    for i in range(10):
        print(next(it3))
