n1, n2 = map(int, input().split())
a = list(map(str, input().split()))
b = list(map(str, input().split()))

def com(x, y):
    return ''.join(y) in ''.join(x)

print("Yes" if com(a, b) else "No")