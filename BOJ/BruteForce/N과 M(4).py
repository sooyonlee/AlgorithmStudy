import sys
n,m = map(int, input().split())
a = [0] * m

def go(idx, start, n, m):
    if idx == m:
        sys.stdout.write(' '.join(map(str, a))+'\n')
        return
    for i in range(start, n+1):
        a[idx] = i
        go(idx+1, i, n, m)
go(0, 1, n, m)