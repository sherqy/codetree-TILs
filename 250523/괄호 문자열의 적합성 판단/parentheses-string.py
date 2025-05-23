str = input()
a = []

# Please write your code here.
for i in str:
    if i == '(':
        a.append(i)
    else:
        if len(a) == 0:
            break
        else:
            a.pop()

if len(a) == 0:
    print("Yes")
else:
    print("No")