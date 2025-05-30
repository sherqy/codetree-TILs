n = int(input())

def star(x):
    if x != 0:
        print("* " * x)
        star(x - 1)
        print("* " * x)

star(n)