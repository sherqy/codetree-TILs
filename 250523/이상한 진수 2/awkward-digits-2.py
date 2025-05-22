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
else:
    print(int(''.join(b), 2))