import sys

ability = list(map(int, input().split()))
ans = sys.maxsize

# Please write your code here.
for i in range(5):
    for j in range(i + 1, 6):

        sum1 = ability[i] + ability[j]

        for k in range(5):
            for l in range(k + 1, 6):
                if i != k and i != l and j != k and j != l:
                    sum2 = ability[k] + ability[l]
                    sum3 = sum(ability) - sum1 - sum2
                    ans = min(max(sum1, sum2, sum3) - min(sum1, sum2, sum3), ans)

print(ans)