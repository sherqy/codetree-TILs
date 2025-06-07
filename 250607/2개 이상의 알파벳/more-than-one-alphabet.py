A = input()

def c(x):
    return "Yes" if x.count(x[0]) != len(x) else "No"

print(c(A))