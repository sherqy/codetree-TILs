a, b = map(int, input().split())

def is_number(x, y):
    ans = 0
    for i in range(x, y + 1):
        if i % 2 != 0 and i % 10 != 5 and i % 3 != 0 or i % 9 == 0:
            ans += 1

    return ans

print(is_number(a, b))