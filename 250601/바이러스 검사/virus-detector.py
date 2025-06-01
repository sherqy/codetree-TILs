n = int(input())
cust = list(map(int, input().split()))
lmax, mmax = map(int, input().split())
ans = 0

for i in cust:
    a = 0

    if i - lmax <= 0:
        ans += 1
    else:
        ans += (i - lmax) // mmax + 2

print(ans)