# BOJ 1926
import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    area = 0
    q = deque()
    visited[i][j] = 1
    q.append((i,j))
    while q:
        x,y = q.popleft()
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx,ny))
    return area
    
n,m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

cnt = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            max_area = max(max_area, bfs(i,j))
print(cnt)
print(max_area)