a, b = map(int, input().split())
n = input()

# Please write your code here.
k = int(n, a)
di = []

while k > 0:
    di.append(str(k % b))
    k = k // b

print(''.join(reversed(di)))