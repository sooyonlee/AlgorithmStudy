# BOJ 7576번
# 시작점이 여러 개인 bfs
from collections import deque

m,n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            # 여기서 bfs를 돌리면 시작점이 하나인 문제가 되는 거임!
            queue.append((i,j))  
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny <0 or nx >= n or ny >=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))   
                
bfs()
cnt = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
print(cnt-1)  