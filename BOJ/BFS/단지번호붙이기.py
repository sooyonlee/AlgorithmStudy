from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]
arr = []
def bfs(i,j):
    sum = 0
    if visited[i][j]:
        return 
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    while q:
        x,y = q.popleft()
        sum += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny]==1 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
    arr.append(sum)
            
n = int(input())
visited = [[False]*n for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

total = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i,j)
            total += 1

print(total)
arr.sort()
for i in arr:
    print(i)