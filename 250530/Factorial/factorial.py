N = int(input())

def fac(x):
    if x == 0:
        return 1
    else:
        return fac(x - 1) * x

print(fac(N))