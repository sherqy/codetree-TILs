n = int(input())
str = input()
ans = 0

# Please write your code here.
for i in range(len(str) - 2):
    if str[i] == 'C':
        for j in range(i + 1, len(str) - 1):
            if str[j] == 'O':
                for k in range(j + 1, len(str)):
                    if str[k] == 'W':
                        ans += 1

print(ans)