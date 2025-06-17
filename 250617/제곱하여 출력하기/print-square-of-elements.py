n = int(input())
m = list(map(int, input().split()))
m = [i * i for i in m]
print(*m)