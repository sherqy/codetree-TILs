str = input()
a = []

# Please write your code here.
for i in str:
    if i == '(':
        a.append(i)
    else:
        if len(a) != 0:
            a.pop()
        else:
            a.append(i)

if len(a) != 0:
    print("No")
else:
    print("Yes")