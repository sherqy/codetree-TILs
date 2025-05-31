a, b, c = map(int, input().split())

def cal(x):
    if x // 10 == 0:
        return x

    return cal(x // 10) + x % 10

print(cal(a * b * c))