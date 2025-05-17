n = int(input())

# Please write your code here.
di = []

while n >= 0:
    di.append(str(n % 2))
    n = n // 2

print(''.join(reversed(di)))