A = input()

def pal(x):
    return "Yes" if x == ''.join(reversed(list(x))) else "No"

print(pal(A))