n = int(input())

def is_digit(x):
    return x % 2 == 0 and (x % 10 + x // 10) % 5 == 0

print("Yes" if is_digit(n) else "No")