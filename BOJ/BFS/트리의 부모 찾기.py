from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([1])
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if parent[i] == 0:
                parent[i] = now
                queue.append(i)

n = int(input())
parent = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()

for i in parent[2:]:
    print(i)