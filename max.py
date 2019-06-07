x, y, z = [int(x) for x in input().split()]
if x>=y:
    if x>z:
        print(x)
    else:
        print(z)
if y>x:
    if y>z:
        print(y)
    else:
        print(z)
