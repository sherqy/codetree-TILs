N = int(input())

def flower(x):
    if x != 0:
        print(x, end = ' ')
        flower(x - 1)
        print(x, end = ' ')

flower(N)