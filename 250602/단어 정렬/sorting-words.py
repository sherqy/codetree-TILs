n = int(input())
word = sorted([input() for _ in range(n)])
print(*word, sep = '\n')