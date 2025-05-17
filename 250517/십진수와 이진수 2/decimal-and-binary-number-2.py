N = int(input(), 2) * 17

# Please write your code here.
di = []

while N > 0:
    di.append(str(N % 2))
    N = N // 2

print(''.join(reversed(di)))