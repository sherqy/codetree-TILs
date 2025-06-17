n = int(input())
arr = []
i = 1
cnt = 0

while cnt != 2:
    arr.append(n * i)
    cnt += 1 if n * i % 5 == 0 else 0
    i += 1
    
print(*arr)