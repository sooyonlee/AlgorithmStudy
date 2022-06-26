# BOJ 1261번
# visited 처리 잊지 말기! -> 시간 초과 발생
# 인덱스 주의! x == n-1 , y == m-1
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(n,m):
    q = deque()
    q.append((0,0))
    graph[0][0] = 1
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        if x == n-1 and y == m-1:
            print(graph[x][y]-1)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]
                    q.appendleft((nx,ny))
                else:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))
                visited[nx][ny] = 1

m,n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
bfs(n,m)