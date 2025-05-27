n = int(input())
people = [''] * 101
max_size = 0

for _ in range(n):
    p, f = map(str, input().split())
    people[int(p)] = f

for i in range(100):
    size = 0

    for j in range(i + 1, 101):
        if people[i] == '' or people[j] == '':
            continue
        else:
            if people[i : j + 1].count('G') == people[i : j + 1].count('H'):
                size = j - i
            elif people[i : j + 1].count('G') == 0 and people[i : j + 1].count('H') > 1:
                size = j - i
            elif people[i : j + 1].count('G') > 1 and people[i : j + 1].count('H') == 0:
                size = j - i

        max_size = max(size, max_size)

print(max_size)