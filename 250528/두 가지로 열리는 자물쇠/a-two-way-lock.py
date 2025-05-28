N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
ans = 0

# Please write your code here.
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if (abs(a1 - i) <= 2 or abs(a1 - i) >= n - 2) and (abs(b1 - j) <= 2 or abs(b1 - j) >= n - 2) and \
               (abs(c1 - k) <= 2 or abs(c1 - k) >= n - 2):
                ans += 1
			
			# 모든 자리가 주어진 두 번째 조합과의 거리가 2 이내인지 확인합니다.
            elif (abs(a2 - i) <= 2 or abs(a2 - i) >= n - 2) and (abs(b2 - j) <= 2 or abs(b2 - j) >= n - 2) and \
               (abs(c2 - k) <= 2 or abs(c2 - k) >= n - 2):
                ans += 1

print(ans)