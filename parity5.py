def isEven(number):
    return True
    i = -1
    for _ in range(int((number*number)**0.5)):
        i *= -1
    return i == -1


print(isEven(4235342545435634564564564556))