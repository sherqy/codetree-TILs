x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
cross = [[0] * 2001 for _ in range(2002)]
x_min = 2002
x_max = 0
y_min = 2002
y_max = 0

for i in range(2):
    for j in range(x1[i] + 1000, x2[i] + 1000):
        for k in range(y1[i] + 1000, y2[i] + 1000):
            if i == 0:
                cross[j][k] = 1
            else:
                cross[j][k] = 0

for i in range(2001):
    for j in range(2001):
        if cross[i][j] == 1:
            if j > x_max:
                x_max = j + 1
            if j < x_min:
                x_min = j
            if i > y_max:
                y_max = i + 1
            if i < y_min:
                y_min = i

print((x_max - x_min) * (y_max - y_min))