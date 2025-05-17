m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cal1 = sum(month[:m1]) + d1 + days.index(A)
cal2 = sum(month[:m2]) + d2
ans = 1

while cal2 > cal1:
    ans += 1
    cal1 += 7

print(ans)