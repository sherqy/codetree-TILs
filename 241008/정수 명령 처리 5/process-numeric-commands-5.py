n = int(input())
m = []

for _ in range(n):
    a = list(map(str, input().split()))

    if a[0] == "push_back":
        m.append(int(a[1]))
    elif a[0] == "pop_back":
        m.pop()
    elif a[0] == "size":
        print(len(m))
    else:
        print(m[int(a[1]) - 1])