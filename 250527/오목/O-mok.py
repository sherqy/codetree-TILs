import sys

board = [list(map(int, input().split())) for _ in range(19)]
winner = 0
dxs, dys = [1, 1, 0, -1, -1, -1, 0, 1], [0, 1, 1, 1, 0, -1, -1, -1]


def in_range(nx, ny):
    return 0 <= nx < 19 and 0 <= ny < 19
# Please write your code here.

for i in range(0, 19):
    for j in range(0, 19):
        for k, l in zip(dxs, dys):
            cnt = []
            for m in range(5):
                if in_range(i + k * m, j + l * m):
                    cnt.append(board[i + k * m][j + l * m])

            if cnt.count(1) == 5 or cnt.count(2) == 5:
                winner = cnt[0]
                print(cnt[0])
                print(i + k * 2 + 1, j + l * 2 + 1)
                sys.exit()

if winner == 0:
    print(winner)