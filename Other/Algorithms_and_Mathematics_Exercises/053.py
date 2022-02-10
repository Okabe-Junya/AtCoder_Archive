# xのn乗をmで割った余り
def pos(x, n, m):
    if n == 0:
        return 1
    res = pos((x ** 2) % m, n // 2, m)
    if n % 2 == 1:
        res = res * x % m
    return res


n = int(input())
INF = 10 ** 9 + 7
res = pos(4, n + 1, INF) - 1
tmp = pow(3, -1, INF)
print(res * tmp % INF)