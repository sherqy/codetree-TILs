ans = 0

for _ in range(3):
    line = input().split()

    if line[0] == 'Y' and int(line[1]) >= 37:
        ans += 1

print("E" if ans >= 2 else "N")