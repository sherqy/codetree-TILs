n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            
            if i == j or j == k or k == i:
                continue
    
            suc = True
            
            for b, cnt1, cnt2 in arr:
                x = [b // 100, (b % 100) // 10, b % 10]
                y, z = 0, 0
                
                if i == x[0]:
                    y += 1
                if i == x[1] or i == x[2]:
                    z += 1
                if j == x[1]:
                    y += 1
                if j == x[0] or j == x[2]:
                    z += 1
                if k == x[2]:
                    y += 1
                if k == x[0] or k == x[1]:
                    z += 1

                if y != cnt1 or z != cnt2:
                    suc = False
                    break
            if suc:
                ans += 1
print(ans)
