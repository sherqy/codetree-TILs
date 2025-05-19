n, m = map(int, input().split())

a = [0] * 1000000
b = [0] * 1000000
pos = 0
index = 0

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

for i in range(1, len(a)):
    if a[i] == b[i]:
        print(i)
        break