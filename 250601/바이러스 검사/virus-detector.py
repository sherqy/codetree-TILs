n = int(input())
cust = list(map(int, input().split()))
lmax, mmax = map(int, input().split())
ans = 0

for i in cust:
    a = i - lmax
    ans += 1

    if a > 0:
        ans += a // mmax if a % mmax == 0 else a //mmax + 1

print(ans)