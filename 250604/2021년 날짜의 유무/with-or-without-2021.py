M, D = map(int, input().split())

def is_date(x, y):
    da = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 1 <= x < 13 and 1 <= y <= da[x]

print("Yes" if is_date(M, D) else "No")