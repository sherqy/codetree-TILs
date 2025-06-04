Y, M, D = map(int, input().split())

def is_yoon(x):
    return x % 4 == 0 and x % 100 != 0 or x % 400 == 0

def is_date(x, y, z):
    da = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    da[2] += 1 if is_yoon(z) else 0

    return 1 <= x <= 12 and 1 <= y <= da[x]

if 3 <= M <= 5 and is_date(M, D, Y):
    print("Spring")
elif 6 <= M <= 8 and is_date(M, D, Y):
    print("Summer")
elif 9 <= M <= 11 and is_date(M, D, Y):
    print("Fall")
elif M == 12 or M <= 2 and is_date(M, D, Y):
    print("Winter")
else:
    print(-1)