n = int(input())

def ascending(n):
    if n != 0:
        ascending(n - 1)
        print(n, end = ' ')

def descending(n):
    if n != 0:
        print(n, end = ' ')
        descending(n - 1)

ascending(n)
print()
descending(n)