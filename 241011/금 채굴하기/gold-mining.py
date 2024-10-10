import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
f = list(list(map(int, input().split())) for _ in range(n))
g = sum(list(sum(i) for i in f))
k = 0
answer = []
total = 0
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direction = []

while k * k + (k + 1) * (k + 1) <= g * m:
    if k == 0:  #k가 0일 경우에는 확실히 답이 1
        answer.append((0, 1))
    else:       #k가 0이 아닐 경우에는 마름모에 따라 탐색
        for i in combinations_with_replacement(dxdy, k):    #k값에 따라 마름모 크기 결정
            x, y = 0, 0
            direction.append((0, 0))
            for j, l in i:
                x += j
                y += l
            direction.append((x, y))
        direction = list(set(direction))    #중복 제거

        #마름모 크기에 따라 탐색하는 과정
        for a in range(n):
            for b in range(n):
                maximum = 0
                for x, y in direction:

                    if a + x >= 0 and a + x < n and b + y >= 0 and b + y < n:
                        if f[a + x][b + y] == 1:
                            maximum += 1
                total = maximum if maximum >= total else total
        answer.append((k, total))
    k += 1

tri = 0

for i, j in answer:
    if j >= tri:
        tri = j

print(tri)