a, b = map(int, input().split())
ans = 0

def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
        
    return True

for i in range(a, b + 1):
    if is_prime(i):
        ans += i

print(ans)