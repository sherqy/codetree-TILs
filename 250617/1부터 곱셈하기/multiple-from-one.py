n = int(input())
ans = 1

for i in range(1, n + 1):
    ans *= i

    if ans >= n:
        print(i)
        break