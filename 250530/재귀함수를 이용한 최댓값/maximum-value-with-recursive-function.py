n = int(input())
arr = list(map(int, input().split()))

def max_val(a):
    if len(a) == 1:
        return a[0]
    
    return max_val(a[0 : len(a) - 1]) if a[-1] < max_val(a[0 : len(a) - 1]) else a[-1]

print(max_val(arr))