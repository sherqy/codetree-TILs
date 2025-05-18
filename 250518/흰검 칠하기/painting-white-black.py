n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

# Please write your code here.
count_B = [0] * 200000
count_W = [0] * 200000
color = ['E'] * 200000
start  = 99999

for i, j in commands:
    if j == 'R':
        for k in range(0, int(i)):
            color[start] = 'B'
            count_B[start] += 1
            start += 1
        start -= 1
    else:
        for k in range(int(i), 0, -1):
            color[start] = 'W'
            count_W[start] += 1
            start -= 1
        start += 1

for i in range(200000):
    if count_B[i] >= 2 and count_W[i] >= 2:
        color[i] = 'G'

white = color.count('W')
black = color.count('B')
gray = color.count('G')

print(white, black, gray)