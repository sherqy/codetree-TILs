n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
line = [0] * 1000
start = 499

for i in range(n):
    if dir[i] == 'R':
        for j in range(x[i]):
            line[start] += 1
            start += 1
    else:
        for j in range(x[i], 0, -1):
            line[start] += 1
            start -= 1

print(line.count(max(line)))