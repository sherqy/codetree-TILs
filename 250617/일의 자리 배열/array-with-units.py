m = list(map(int, input().split()))

for _ in range(8):
    m.append((m[-1] + m[-2]) % 10)

print(*m)