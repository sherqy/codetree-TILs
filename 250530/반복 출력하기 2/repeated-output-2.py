n = int(input())

def print_hello(x):
    if x == 0:
        return
    else:
        print("HelloWorld")
        print_hello(x - 1)

print_hello(n)