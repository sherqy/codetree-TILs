binary = list(map(int, str(input())))

# Please write your code here.
ans = 0

for i in binary:
    ans = ans * 2 + i

print(ans)