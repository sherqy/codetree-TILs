N = int(input())

def fibbo(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fibbo(x - 1) + fibbo(x - 2)

print(fibbo(N))