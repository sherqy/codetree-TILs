m = list(map(int, input().split()))

for i in m:
    if i == 0:
        break
    
    print(i + 3 if i % 2 == 1 else i // 2, end = ' ')