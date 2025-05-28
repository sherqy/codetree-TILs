import sys

abilities = list(map(int, input().split()))
ans = sys.maxsize

def get_diff(x, y, z):
    sum1 = x + y + z
    sum2 = abs(sum(abilities) - sum1)
    return abs(sum1 - sum2)

for i in range(4):
    for j in range(i + 1, 5):
        for k in range(j + 1, 6):
            ans = min(ans, get_diff(i, j, k))

print(ans)