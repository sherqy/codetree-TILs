n = int(input())
arr = list(map(int, input().split()))

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y):
    if len(arr) == 1:
        return arr[0]
    if y == len(arr) - 1:
        return x

    x = x * arr[y + 1] // gcd(x, arr[y + 1]) 
    return lcm(x, y + 1)

print(lcm(arr[0], 0))