import sys

arr = list(map(int, input().split()))
ans = sys.maxsize

# Please write your code here.
for i in range(5):
    team1 = sum([arr[i]])

    for j in range(4):
        for k in range(j + 1, 5):
            if j != i and k != i:
                team2 = sum([arr[j], arr[k]])
                team3 = sum(arr) - team1 - team2

                if team1 != team2 and team1 != team3 and team2 != team3:
                    ans = min(ans, max(team1, team2, team3) - min(team1, team2, team3))
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)