N, M = map(int, input().split())
arr = [input() for _ in range(N)]
dxs, dys = [1, 1, 0, -1, -1, -1, 0, 1], [0, 1, 1, 1, 0, -1, -1, -1]
ans = 0

def in_range(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

# Please write your code here.
for i in range(N):
    for j in range(M):
        for k, l in zip(dxs, dys):
            string = ''
            for m in range(3):
                if in_range(i + k * m, j + l * m):
                    string += arr[i + k * m][j + l * m]
                
            if string == 'LEE':
                ans += 1

print(ans)