# BOJ 13549
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
# -> 가중치가 다름. 시간이 짧은 경우 우선순위가 높다.
from collections import deque
import sys
input = sys.stdin.readline

def bfs(n,k):
    q = deque()
    q.append(n)
    graph[n] = 1
    while q:
        x = q.popleft()
        if x == k:
            print(graph[x]-1)
            return
        for nx in (x-1, x+1, 2*x):
            if nx < 0 or nx >= 200001:
                continue
            if graph[nx] == 0:
                if x == 2*nx:
                    graph[nx] = graph[x]
                    q.appendleft(nx)
                else:
                    graph[nx] = graph[x]+1
                    q.append(nx)

n,k = map(int, input().split())
graph = [0] * 200001
bfs(n,k)