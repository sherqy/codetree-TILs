n = int(input())

# Please write your code here.
di = []

if n > 0:
    while n > 0:
        di.append(str(n % 2))
        n = n // 2
else:
    di.append('0')

print(''.join(reversed(di)))