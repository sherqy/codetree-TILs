n = int(input())
direction = {
    'N' : 0,
    'E' : 1,
    'S' : 2,
    'W' : 3
}
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
init = [0, 0]
answer = 0
flag = 0

for i in range(n):
    d, r = map(str, input().split())

    for _ in range(int(r)):
        init[0], init[1] = init[0] + dxs[direction[d]], init[1] + dys[direction[d]]
        answer += 1

        if init[0] == 0 and init[1] == 0:
            print(answer)
            flag = 1
            break
if flag == 0:
    print(-1)