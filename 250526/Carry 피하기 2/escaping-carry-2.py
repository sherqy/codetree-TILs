n = int(input())
arr = [int(input()) for _ in range(n)]
ans = -1

# Please write your code here.
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            a, b, c = arr[i], arr[j], arr[k]
            
            while a != 0 or b != 0 or c != 0:
                if a % 10 + b % 10 + c % 10 < 10:
                    a = a // 10
                    b = b // 10
                    c = c // 10
                else:
                    break
            
            if a == 0 and b == 0 and c == 0:
                ans = max(ans, arr[i] + arr[j] + arr[k])

print(ans)