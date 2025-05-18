n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
tiles = ['E'] * 200000
start = 99999

# Please write your code here.
for i, j in commands:
    if j == 'R':
        for k in range(0, int(i)):
            tiles[start] = 'B'
            start += 1
        start -= 1
    else:
        for k in range(int(i), 0, -1):
            tiles[start] = 'W'
            start -= 1
        start += 1

print(tiles.count('W'), tiles.count('B'))