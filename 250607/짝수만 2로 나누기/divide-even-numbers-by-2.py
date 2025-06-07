n = int(input())
arr = list(map(int, input().split()))

def even(x):
    for i in range(len(x)):
        if x[i] % 2 == 0:
            x[i] //= 2

    return x

arr = even(arr)
print(*arr)