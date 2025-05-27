import sys

N, H, T = map(int, input().split())
arr = list(map(int, input().split()))
min_val = sys.maxsize

for i in range(N - T):
    h = 0
    
    for j in range(i, i + T):
        h += abs(H - arr[j])

    min_val = min(h, min_val)

print(min_val)