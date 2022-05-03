import sys
n,m = map(int, input().split())
visited = [False]*(n+1)
a = [0] * m

def go(idx, start, n, m):
    if idx == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
    for i in range(start, n+1):
        if visited[i]:
            continue
        visited[i] = True
        a[idx] = i
        go(idx + 1, i+1, n, m)
        visited[i] = False

go(0, 1, n, m)