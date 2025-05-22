a = input()
b = []

# Please write your code here.
for i in range(len(a)):
    if a[i] == '0':
        b.append('1')
        break
    else:
        b.append(a[i])

b.append(a[i + 1 : ])

if a == '1':
    print(0)
elif not('0' in a):
    print(int(''.join(a[ : len(a) - 1] + '0'), 2))
else:
    print(int(''.join(b), 2))