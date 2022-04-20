import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, v, visited):
    if visited[v] == 1:
        return False
    queue = deque([v])
    visited[v] = 1
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    return True

n,m = map(int, input().split())
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, n+1):
    if bfs(graph, i, visited) == True:
        cnt += 1
print(cnt)