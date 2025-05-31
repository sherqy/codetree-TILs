import sys

dxs=[-1,-1,1,1]
dys=[1,-1,-1,1]

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def get_score(x, y, w, h):
    move_size = [w, h, w, h]
    
    total = 0
    for dx, dy, length in zip(dxs, dys, move_size):
        for _ in range(length):
            x = x + dx
            y = y + dy
            
            if not in_range(x, y):
                return 0

            total += board[x][y]
    
    return total
            
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        for w in range(1, n):
            for h in range(1, n):
                ans = max(ans, get_score(i, j, w, h))    
    
print(ans)