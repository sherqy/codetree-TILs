x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
cross = [[0] * 2001 for _ in range(2002)]
x_pos = 0
x_max = 0
x_min = 0
y_min = 0
y_max = 0
min_flag = 0
max_flag = 0

for i in range(2):
    for j in range(x1[i] + 1000, x2[i] + 1000):
        for k in range(y1[i] + 1000, y2[i] + 1000):
            if i == 0:
                cross[j][k] = 1
            else:
                cross[j][k] = 0

for i in cross:
    if sum(i) > x_max:
        x_min = i.index(1)
        x_max = i.index(1)
        for j in range(x_min, 2001):
            if i[j] == 1 and x_max < j:
                x_max = j

x_pos = x_max - x_min + 1

for i in range(2001):
    for j in range(2001):
        if cross[i][j] == 1:
            y_min = i
            min_flag = 1
            break
    if min_flag == 1:
        break

for i in range(2000, -1, -1):
    for j in range(2000, -1, -1):
        if cross[i][j] == 1:
            y_max = i
            max_flag = 1
            break
    if max_flag == 1:
        break

large = 0

for i in cross:
    large += sum(i)

if large == 0:
    print(0)
else:    
    print(x_pos * (y_max - y_min + 1))