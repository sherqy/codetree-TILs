a, b = map(int, input().split())

def is_number(x, y):
    ans = 0
    for i in range(x, y + 1):
        if i % 2 == 0:
            ans += 0
        elif i % 10 == 5:
            ans += 0
        elif i % 3 == 0 and i % 9 != 0:
            ans += 0
        else:
            ans += 1
    return ans

print(is_number(a, b))