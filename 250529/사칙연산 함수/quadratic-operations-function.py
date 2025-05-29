a, o, c = input().split()
a = int(a)
c = int(c)

def calc(x, y, z):
    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '/':
        return x // z
    elif y == '*':
        return x * z

if o in ['+', '-', '/', '*']:
    print(f'{a} {o} {c} = {calc(a, o, c)}')
else:
    print(False)