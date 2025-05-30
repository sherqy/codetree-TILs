N = int(input())

def square(x):

    if x < 10:
        return x ** 2
    
    return square(x // 10) + (x % 10) ** 2

print(square(N))