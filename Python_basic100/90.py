# 문제가 길어서 생략

a, m, d, n = map(int, input().split())
s = a

for _ in range(n-1):
    s = (s*m)+d

print(s)