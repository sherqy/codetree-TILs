a, b = map(int, input().split())
ans = 0

def is_prime(n):
    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(a, b + 1):
    if is_prime(i) and (i // 10 + i % 10) % 2 == 0:
        ans += 1

print(ans)