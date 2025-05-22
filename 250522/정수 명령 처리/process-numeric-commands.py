N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    elif line[0] == "pop":
        print(value.pop())
    elif line[0] == "size":
        print(len(value))
    elif line[0] == "empty":
        print(1 if len(value) == 0 else 0)
    else:
        print(value[-1])