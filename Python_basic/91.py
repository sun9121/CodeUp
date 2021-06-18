# 문제가 너무 길어서 생략

a, b, c = map(int, input().split())

for i in range(1, a*b*c+1):
    if i % a == 0:
        if i % b == 0:
            if i % c == 0:
                print(i)
                break