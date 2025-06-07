a = ["apple", "banana", "grape", "blueberry", "orange"]
ans = 0
b = input()

for i in a:
    if i[2] == b or i[3] == b:
        print(i)
        ans += 1

print(ans)