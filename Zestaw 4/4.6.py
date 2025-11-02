def sum_seq(sequence):
    suma = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            suma += sum_seq(i) 
        else:
            suma += i
    return suma

print(sum_seq([1,2,3,4]))
print(sum_seq([1,2,(3,4)]))
print(sum_seq([([1,2],3),4]))