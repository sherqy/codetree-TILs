n = int(input())
arr = list(map(int, input().split()))

def ab(x):
    for i in x:
        print(abs(i), end = ' ')

ab(arr)