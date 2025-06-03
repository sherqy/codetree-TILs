y = int(input())

if y % 4 == 0:
    print("true" if y % 100 != 0 or y % 400 == 0 else "false")
else:
    print("false")