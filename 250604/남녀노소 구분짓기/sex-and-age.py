s = int(input())
a = int(input())

if s == 0:
    print("MAN" if a >= 19 else "BOY")
else:
    print("WOMAN" if a >= 19 else "GIRL")