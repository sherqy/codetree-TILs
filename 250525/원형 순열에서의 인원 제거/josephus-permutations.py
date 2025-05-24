n, k = map(int, input().split())

# Please write your code here.
from collections import deque

class queue:
    def __init__(self):
        self.dq = deque()
    def push(self, x):
        self.dq.append(x)
    def empty(self):
        return 1 if len(self.dq) == 0 else 0
    def size(self):
        return len(self.dq)
    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq.popleft()
    def front(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq[0]

p = queue()

for i in range(1, n + 1):
    p.push(i)

i = 1
while not p.empty():
    if i == k:
        print(p.pop(), end = ' ')
        i = 1
    else:
        p.push(p.pop())
        i += 1