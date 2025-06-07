a, b = map(int, input().split())

while a <= b:
    print(a, end = ' ')
    a = a * 2 if a % 2 == 1 else a + 3