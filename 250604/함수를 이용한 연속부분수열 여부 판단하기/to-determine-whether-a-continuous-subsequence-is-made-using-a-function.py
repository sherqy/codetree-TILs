n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def com(x, y):
    for i in range(n1 - n2):
        if x[i : i + n2] == y:
            return True
    return False

print("Yes" if com(a, b) else "No")