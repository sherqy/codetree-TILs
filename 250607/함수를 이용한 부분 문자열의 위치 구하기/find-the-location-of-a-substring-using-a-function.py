text = input()
pattern = input()
flag = 0

for i in range(len(text) - len(pattern) + 1):
    if text[i : i + len(pattern)] == pattern:
        print(i)
        flag = 1
        break

if flag == 0:
    print(-1)