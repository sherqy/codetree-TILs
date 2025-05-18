n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
line = [0] * 1001
start = 500

for i in range(n):
    if dir[i] == 'R':
        for j in range(x[i]):
            line[start] += 1
            start += 1
    else:
        for j in range(x[i], 0, -1):
            start -= 1
            line[start] += 1  

print(1001 - line.count(0) - line.count(1))