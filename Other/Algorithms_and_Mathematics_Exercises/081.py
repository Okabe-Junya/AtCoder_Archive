N = int(input())
ans = 0
ans += N // 10000
N -= ans * 10000
ans += N // 5000
N -= (N // 5000) * 5000
ans += N // 1000
print(ans)