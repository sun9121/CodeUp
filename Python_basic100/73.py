# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

n = int(input())

for _ in range(n):
    n -= 1
    print(n)