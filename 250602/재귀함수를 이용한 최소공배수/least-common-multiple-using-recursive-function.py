n = int(input())
arr = list(map(int, input().split()))
g = arr[0]

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y):
    if y == len(arr) - 1:
        return 1
    return lcm(x, y + 1) * arr[y] // x

for i in range(len(arr) - 1):
    g = gcd(g, arr[i + 1])

print(lcm(g, 0))