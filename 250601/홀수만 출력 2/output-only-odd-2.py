a, b = map(int, input().split())
print(*[i for i in range(a, b - 1, -2)])