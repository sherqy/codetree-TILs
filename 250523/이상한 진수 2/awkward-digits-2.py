a = list(map(int, list(input())))

max_val = 0

for i in range(len(a)):
    a[i] = int(not a[i])

    max_val = max(max_val, int(''.join(map(str, a)), 2))

    a[i] = int(not a[i])

print(max_val)