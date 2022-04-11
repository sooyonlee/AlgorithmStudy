from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    print(v, end=' ')
    visited[v] = True
    for i in sorted(graph[v]):
        if visited[i] == False:
            dfs(graph, i, visited)
            
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        a = queue.popleft()
        print(a, end=' ')
        for i in sorted(graph[a]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True
   
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)    
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)
