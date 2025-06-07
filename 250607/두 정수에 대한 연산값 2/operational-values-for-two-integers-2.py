a, b = map(int, input().split())

def swap(x, y):
    if x > y:
        x, y = x * 2, y + 10
    else:
        x, y = x + 10, y * 2

    return x, y

a, b = swap(a, b)
print(a, b)