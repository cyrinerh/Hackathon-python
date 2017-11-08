
def multiply (l):
    s=1
    for el in l:
        if type(el) == int:
            s = s * int(el)
    if type(el) != int:
        print('enter only numbers')
    return s
