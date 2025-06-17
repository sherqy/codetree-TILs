n = int(input())

for i in range(1, n + 1):
    for j in range(1, n):
        print(f"{i} * {j} = {i * j}, ", end = '')
    print(f"{i} * {j + 1} = {i * (j + 1)}")