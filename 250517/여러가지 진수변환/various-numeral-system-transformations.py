N, B = map(int, input().split())

# Please write your code here.
di = []
while N > 0:
    di.append(str(N % B))
    N = N // B

print(''.join(reversed(di)))