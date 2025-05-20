N, M = map(int, input().split())
pos_a = [0] * 1000001
pos_b = [0] * 1000001
time = 1
first = ''
ans = 0

for _ in range(N):
    v, t = map(int, input().split())
    
    for i in range(1, t + 1):
        pos_a[time] += pos_a[time - 1] + v
        time += 1

time = 1

for _ in range(M):
    v, t = map(int, input().split())
    
    for i in range(1, t + 1):
        pos_b[time] += pos_b[time - 1] + v
        time += 1

for i in range(1, time):
    if pos_a[i] > pos_b[i] and first != 'A':
        first = 'A'
        ans += 1
    elif pos_b[i] > pos_a[i] and first != 'B':
        first = 'B'
        ans += 1
    elif pos_a[i] == pos_b[i] and first != 'AB':
        first = 'AB'
        ans += 1

print(ans)