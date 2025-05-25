s = int(input())
a = int(input())

if s == 0 and a >= 19:
    print("MAN")
elif s == 1 and a >= 19:
    print("WOMAN")
elif s == 0 and a < 19:
    print("BOY")
else:
    print("GIRL")