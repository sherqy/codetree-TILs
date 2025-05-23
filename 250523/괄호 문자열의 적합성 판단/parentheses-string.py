str = input()
a = []
flag = 0

# Please write your code here.
for i in str:
    if i == '(':
        a.append(i)
        flag = 1
    else:
        if len(a) == 0:
            break
        else:
            a.pop()

if len(a) == 0 and flag == 1:
    print("Yes")
else:
    print("No")