n, m = map(int, input().split())
pos_a = [0] * 1000001
pos_b = [0] * 1000001
time = 1
ans = 0

for _ in range(n):
    vi, ti = map(int, input().split())

    for i in range(1, ti + 1):
        pos_a[time] += pos_a[time - 1] + vi
        time += 1

# Process B's movements
time = 1

for _ in range(m):
    vi, ti = map(int, input().split())

    for i in range(1, ti + 1):
        pos_b[time] += pos_b[time - 1] + vi
        time += 1

count = [''] * time

for i in range(1, time):
    count[i] = '-' if pos_a[i] - pos_b[i] < 0 else '+'

for i in range(1, time - 1):
    if count[i] != count[i + 1]:
        ans += 1

print(ans)