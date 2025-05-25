from collections import deque

n = int(input())
num = deque([i for i in range(1, n + 1)])
# Please write your code here.

while len(num) != 1:
    num.popleft()
    num.append(num.popleft())

print(num[0])