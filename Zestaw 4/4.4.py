def fibonacci(n):
    pierwszy = 0
    drugi = 1
    nty = 0

    if n<0:
        raise ValueError("nie ma liczby fibonacciego dla liczb ujemnych")

    elif n == 0:
        return pierwszy

    elif n == 1:
        return drugi

    for i in range(2,n+1):
        nty = pierwszy + drugi
        pierwszy = drugi 
        drugi = nty

    return nty

print(fibonacci(4))