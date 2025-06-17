cnt = [0] * 7
arr = list(map(int, input().split()))

for i in arr:
    cnt[i] += 1

for i in range(6):
    print(f"{i + 1} - {cnt[i + 1]}")