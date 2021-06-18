# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

# 예시
# n = int(input())
# for i in range(n+1) :
#   print(i)

# 참고
# range(n) 은 0, 1, 2, ... , n-2, n-1 까지의 수열을 의미한다.
# 예를 들어 range(3) 은 0, 1, 2 인 수열을 의미한다.

n = int(input())
i = 0

for i in range(n+1):
    print(i)
    i += 1