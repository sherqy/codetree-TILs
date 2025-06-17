cnt = [0] * 4

for _ in range(3):
    a, b = input().split()
    b = int(b)

    if a == 'Y' and b >= 37:
        cnt[0] += 1
    elif a == 'Y' and b < 37:
        cnt[2] += 1
    elif a == 'N' and b >= 37:
        cnt[1] += 1
    else:
        cnt[3] += 1

print(*cnt, end = ' ')
print('E' if cnt[0] >= 2 else '')