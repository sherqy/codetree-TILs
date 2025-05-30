n = int(input())

def print_star(x):
    if x != 0:
        print_star(x - 1)
        print("*" * x)

print_star(n)