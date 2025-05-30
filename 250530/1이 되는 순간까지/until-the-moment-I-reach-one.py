N = int(input())

def calc(x):

    if x == 1:
        return 0

    if x % 2 == 0:
        return calc(x // 2) + 1
    else:
        return calc(x // 3) + 1

print(calc(N))