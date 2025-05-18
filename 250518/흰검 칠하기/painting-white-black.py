n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

# Please write your code here.
line = [0] * 200000
color = ['E'] * 200000
start  = 99999

for i, j in commands:
    if j == 'R':
        for k in range(0, int(i)):
            color[start] = 'B'
            line[start] += 1
            start += 1
        start -= 1
    else:
        for k in range(int(i), 0, -1):
            color[start] = 'W'
            line[start] += 1
            start -= 1
        start += 1

for i in range(len(line)):
    if line[i] >= 4:
        color[i] = 'G'

white = color.count('W')
black = color.count('B')
gray = color.count('G')

print(white, black, gray)