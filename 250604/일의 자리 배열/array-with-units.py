a, b = map(int, input().split())

for _ in range(10):
    print(a, end = ' ')
    a, b = b, (a + b) % 10