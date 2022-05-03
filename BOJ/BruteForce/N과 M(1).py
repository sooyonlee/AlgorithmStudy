import sys
n,m = map(int, input().split())
visited = [False]*(n+1)
a = [0] * m

def go(idx, n, m):
    if idx == m:
        sys.stdout.write(' '.join(map(str, a))+'\n')
        return
    for i in range(1, n+1):
        if visited[i]: 
            continue
        visited[i] = True
        a[idx] = i
        go(idx+1, n, m)
        visited[i] = False

go(0, n, m)