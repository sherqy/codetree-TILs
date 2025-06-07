y = int(input())

def is_yoon(x):
    return "true" if y % 4 == 0 and not(y % 100 == 0 and y % 400 != 0) else "false"

print(is_yoon(y))