ans_3 = 0
ans_5 = 0

for _ in range(10):
    a = int(input())

    if a % 3 == 0:
        ans_3 += 1
    if a % 5 == 0:
        ans_5 += 1

print(ans_3, ans_5)