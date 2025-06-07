a, b = map(int, input().split())

def cal(x, y):
    if a > b:
        print(a + 25, b * 2)
    else:
        print(a * 2, b + 25)
        
cal(a, b)