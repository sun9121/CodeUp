# 문제가 길어서 생략

ant = []

for i in range(10):
    ant.append(list(map(int, input().split())))

x = 1
y = 1

while True:
    if(ant[x][y] == 0):
        ant[x][y] = 9
    elif (ant[x][y] == 2):
        ant[x][y] = 9
        break

    if (ant[x][y+1] == 1 and ant[x+1][y] == 1):
        break

    if (ant[x][y+1] != 1):
        y = y + 1
    elif (ant[x+1][y] != 1):
        x = x + 1

for i in range(10):
    for j in range(10):
        print(ant[i][j], end=' ')
    print()