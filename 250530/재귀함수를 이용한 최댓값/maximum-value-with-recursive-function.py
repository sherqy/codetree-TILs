n = int(input())
arr = list(map(int, input().split()))

def max_val(a):
    if len(a) == 1:
        return a[0]
    
    b = max_val(a[0 : len(a) - 1])
    return b if a[-1] < b else a[-1]

print(max_val(arr))