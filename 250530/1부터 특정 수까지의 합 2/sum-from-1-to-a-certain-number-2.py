N = int(input())

def total(x):
    if x != 0:
        x += total(x - 1)
    return x

print(total(N))