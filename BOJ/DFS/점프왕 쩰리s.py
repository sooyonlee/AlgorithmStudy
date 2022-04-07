import sys
input=sys.stdin.readline

def dfs(x,y):
    if x<0 or y<0 or x>=N or y>=N:
        return 
    if visited[x][y]==1:
        return 
    if graph[x][y] == -1:
        visited[x][y] = 1
        return
    visited[x][y] = 1
    
    dfs(x+graph[x][y],y)
    dfs(x, y+graph[x][y])
    
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dfs(0,0)

if visited[-1][-1] ==1:
    print("HaruHaru")
else:
    print("Hing")