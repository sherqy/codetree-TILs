n = int(input())

def pp(x):
    ans = 0

    for i in range(x + 1):
        ans += i

    return ans // 10

print(pp(n))