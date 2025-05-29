n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def insertion_sort(x):
    
    for i in range(1, len(x)):
        j = i - 1
        key = x[i]

        while j >= 0 and x[j] > key:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key
    return x

print(*insertion_sort(arr))