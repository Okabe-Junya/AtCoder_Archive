def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n
# 最小公倍数


def lcm(m, n):
    return (m * n // gcd(m, n))


n = int(input())
ans = 1
for i in range(n):
    ans = lcm(i+1, ans)
print(ans + 1)
