from collections import deque
import sys
input = sys.stdin.readline

dx = [2,2,1,1,-2,-2,-1,-1]
dy = [1,-1,2,-2,1,-1,2,-2]

def bfs(a,b,c,d,l):
    q = deque()
    q.append((a,b))
    graph[a][b] = 1
    while q:
        x,y = q.popleft()
        if x == c and y == d:
            return graph[x][y]-1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

n = int(input())
for _ in range(n):
    l = int(input())
    a,b = map(int, input().split())
    c,d = map(int, input().split())
    graph = [[0] * l for _ in range(l)]
    print(bfs(a,b,c,d,l))