N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
ans = 0

def in_dial(m, n):
    if abs(m - n) <= 2 or 1 <= N - abs(m - n) <= 2:
        return True

def unlock(x, y, z):
    if in_dial(a1, x) and in_dial(b1, y) and in_dial(c1, z):
        return True
    elif in_dial(a2, x) and in_dial(b2, y) and in_dial(c2, z):
        return True

# Please write your code here.
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if unlock(i, j, k):
                ans += 1

print(ans)