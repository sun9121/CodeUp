# 임의의 정수가 줄을 바꿔 계속 입력된다.
# -2147483648 ~ +2147483647, 단 개수는 알 수 없다.

# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

n = 1

while n!=0:
    n = int(input())
    if n != 0:
        print(n)

# 포문으로 무한을 돌릴 수는 없을까
# 그냥 20만 정도로 하니까 통과되긴했는데
# for _ in range (200000):
#     n = int(input())
#     if n != 0:
#         print(n)
#     else:
#         break