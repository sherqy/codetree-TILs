n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

print("Yes" if A == B else "No")