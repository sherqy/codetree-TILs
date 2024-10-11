n = int(input())
dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
init = [0, 0]

for _ in range(n):
    d, i = map(str, input().split())

    if d == 'N':
        init[1] += dxdy[0][1] * int(i)
    elif d == 'E':
        init[0] += dxdy[1][0] * int(i)
    elif d == 'S':
        init[1] += dxdy[2][1] * int(i)
    else:
        init[0] += dxdy[3][0] * int(i)

print(init[0], init[1])