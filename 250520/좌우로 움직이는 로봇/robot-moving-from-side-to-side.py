n, m = map(int, input().split())
pos_a = [0] * 1000001
pos_b = [0] * 1000001
time = 1
max_time = 0
count = 0

for _ in range(n):
    t, d = input().split()

    for i in range(int(t)):
        pos_a[time] += pos_a[time - 1] + (1 if d == 'R' else -1)
        time += 1

max_time = time
time = 1

for _ in range(m):
    t, d = input().split()

    for i in range(int(t)):
        pos_b[time] += pos_b[time - 1] + (1 if d == 'R' else -1)
        time += 1

for i in range(1, max(max_time, time) + 1):
    if pos_a[i - 1] != pos_b[i - 1] and pos_a[i] == pos_b[i]:
        count += 1

print(count)