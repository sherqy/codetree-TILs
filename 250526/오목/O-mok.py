board = [list(map(int, input().split())) for _ in range(19)]
winner = 0

# Please write your code here.

for i in range(0, 19):
    for j in range(0, 19):
        same_row, same_col, same_cross = 0, 0, 0
        
        if board[i][j] != 0:
            if j <= 14 and board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == board[i][j + 4]:
                print(board[i][j + 2])
                print(i + 1, j + 3)
                winner = board[i][j + 2]
            if i <= 14 and board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] == board[i + 4][j]:
                print(board[i + 2][j])
                print(i + 3, j + 1)
                winner = board[i + 2][j]
            if i <= 14 and j <= 14 and board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == board[i + 4][j + 4]:
                print(board[i + 2][j + 2])
                print(i + 3, j + 3)
                winner = board[i + 2][j + 2]

if winner == 0:
    print(winner)