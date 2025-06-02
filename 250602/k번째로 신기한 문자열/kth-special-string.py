n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
di = []

for i in str:
    if i.startswith(t):
        di.append(i)

print(sorted(di)[k - 1])