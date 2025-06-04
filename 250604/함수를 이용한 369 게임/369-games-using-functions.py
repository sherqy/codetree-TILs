a, b = map(int, input().split())
ans = 0

def cal2(x):
    return "3" in str(x) or "6" in str(x) or "9" in str(x)

def cal(x):
    return x % 3 == 0 or cal2(x)

for i in range(a, b + 1):
    if cal(i):
        ans += 1

print(ans)