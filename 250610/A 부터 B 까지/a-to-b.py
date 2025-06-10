a, b = map(int, input().split())

while a <= b:
    if a % 2 == 1:
        print(a, end = ' ')
        a *= 2
    else:
        print(a, end = ' ')
        a += 3