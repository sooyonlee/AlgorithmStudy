# BOJ 13913
from collections import deque
import sys
input = sys.stdin.readline

def path(x):
    arr = []
    temp = x
    for _ in range(graph[x]):
        arr.append(temp)
        temp = trace[temp]
    return print(" ".join(map(str, arr[::-1])))

def bfs(n,k):
    q = deque()
    q.append(n)
    graph[n] = 1
    while q:
        x = q.popleft()
        if x == k:
            print(graph[x]-1)
            path(x)
            exit(0)
        for nx in (x-1, x+1, 2*x):
            if nx < 0 or nx >= 200001:
                continue
            if graph[nx] == 0:
                q.append(nx)
                graph[nx] = graph[x] + 1
                trace[nx] = x

n,k = map(int, input().split())
graph = [0] * 200001
trace = [0] * 200001
bfs(n,k)