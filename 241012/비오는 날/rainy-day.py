class data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
m = [
    tuple(map(str, input().split())) for _ in range(n)
]
min_idx = -1

for i in range(0, n - 1):
    if m[i][2] == "Rain":
        if min_idx < 0:
            min_idx = i
        else:
            min_idx = i if m[i][0] < m[min_idx][0] else min_idx


print(f"{m[min_idx][0]} {m[min_idx][1]} {m[min_idx][2]}")