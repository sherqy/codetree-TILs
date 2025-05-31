n = int(input())

def cal(x):
    if x == 1:
        return 0

    return cal(x // 2) + 1 if x % 2 == 0 else cal(3 * x + 1) + 1

print(cal(n))