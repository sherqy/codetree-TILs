grid1 = [list(map(int, input().split())) for _ in range(4)]
grid2 = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(grid1[i][j] * grid2[i][j], end = ' ')
    print()