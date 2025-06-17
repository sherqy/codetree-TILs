cnt = [0] * 10
arr = list(map(int, input().split()))

for i in arr:
    if i == 0:
        break
    cnt[i // 10] += 1

for i in range(9):
    print(f"{i + 1} - {cnt[i + 1]}")