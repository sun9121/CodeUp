# n,m을 받아준다.
# 미로의 출구가 (n,m)으로 미로의 크기도 그와 같다
# 시작은 1,1
# 탈출하기 위해 움직이는 칸의 개수, 시작이랑 마지막 포함 시작부터 1
n, m = map(int, input().split())

# 미로 정보 입력
maze = []
for _ in range(n):
    maze.append(list(map(int, input().split()))) # 괴물(가지 못하는 부분)은 0, 없는 부분은 1

# BFS 방식
def bfs(x,y):
    