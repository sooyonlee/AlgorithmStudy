def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

n = int(input())
m = int(input())

visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
dfs(graph, 1, visited)
print(sum(visited)-1)