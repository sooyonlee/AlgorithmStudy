# BOJ 2178
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    q = deque()
    q.append((0,0))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))
    return graph[n-1][m-1]

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

print(bfs())