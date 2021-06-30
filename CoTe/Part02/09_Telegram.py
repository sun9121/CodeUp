import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

# djikstra
board = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x,y,z = map(int, input().split())
    