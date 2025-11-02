def it_odwracanie(L, left, right):
    while left < right:
        pomocna = L[left]
        L[left] = L[right]
        L[right] = pomocna
        left += 1
        right -= 1
    return L 

def rek_odwracanie(L, left, right):
    if left >= right:
        return L
    pomocna = L[left]
    L[left] = L[right]
    L[right] = pomocna
    rek_odwracanie(L, left+1, right-1)

L = [1, 2, 3, 4, 5, 6]

print("L: ", L)
print("odwrocone od 3 do 5: ", it_odwracanie(L, 3, 5))
L2 = [1, 2, 3, 4, 5, 6]
rek_odwracanie(L2, 0, 5)
print("odwrocone cale ", L2)