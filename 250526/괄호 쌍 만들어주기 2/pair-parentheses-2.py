A = input()
ans = 0

# Please write your code here.
for i in range(len(A) - 2):
    if A[i] == '(' and A[i] == A[i + 1]:
        for j in range(i + 2, len(A) - 1):
            if A[j] == ')' and A[j] == A[j + 1]:
                ans += 1

print(ans)