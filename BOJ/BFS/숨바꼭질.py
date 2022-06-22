# BOJ 1697
from collections import deque
import sys
input = sys.stdin.readline

def bfs(n,k):
    q = deque([n])
    graph[n] = 1
    while q:
        x = q.popleft()
        if x == k:
            print(graph[x]-1)
            exit(0) 
        dx = [1, -1, x]
        for i in range(3):
            nx = x + dx[i]
            if nx < 0 or nx >= 200001:
                continue
            if graph[nx] == 0:
                graph[nx] = graph[x] + 1
                q.append(nx)
            
n,k = map(int, input().split())
graph = [0] * 200001
bfs(n,k)