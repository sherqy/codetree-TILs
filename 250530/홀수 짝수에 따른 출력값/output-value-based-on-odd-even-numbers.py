N = int(input())

def total(x):
    if x < 0:
        return 0

    return total(x - 2) + x

print(total(N))