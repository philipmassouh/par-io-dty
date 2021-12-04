from functools import reduce

def isEven(number):
    reverse_lookup = (-1, 0)
    return list(map(lambda x: x[0], [reverse_lookup:=(reverse_lookup[0]*-1, i) for i in range(number)]))[-1] == -1

print(isEven(12))