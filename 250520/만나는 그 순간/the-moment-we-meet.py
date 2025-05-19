n, m = map(int, input().split())

a = [0] * 1000000
b = [0] * 1000000
a_final = 0
b_final = 0
pos = 0
index = 0
ans = -1

for _ in range(n):
    direction, time = input().split()
    
    for i in range(1, int(time) + 1):
        if direction == 'R':
            pos += 1
            index += 1
            a[index] = pos
        else:
            pos -= 1
            index += 1
            a[index] = pos

a_final = index
pos = 0
index = 0

for _ in range(m):
    direction, time = input().split()
    
    for i in range(1, int(time) + 1):
        if direction == 'R':
            pos += 1
            index += 1
            b[index] = pos
        else:
            pos -= 1
            index += 1
            b[index] = pos

b_final = index

for i in range(1, max(a_final, b_final)):
    if a[i] == b[i]:
        ans = i
        break

print(ans)