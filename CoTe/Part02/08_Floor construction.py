# 바닥의 크기 =  가로 n * 세로 2 (1<=n<=1000)
n = int(input())
# # dp 테이블 만들기(3<=n<=1000)
d = [0]*1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]*2) % 796796

print(d[n])