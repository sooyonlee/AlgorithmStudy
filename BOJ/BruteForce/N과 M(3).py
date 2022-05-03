import sys
n,m = map(int, input().split())
a = [0] * m

def go(idx, n, m):
    if idx == m:
        sys.stdout.write(' '.join(map(str, a))+'\n')
        return
    for i in range(1, n+1):
        a[idx] = i
        go(idx+1, n, m)
go(0, n, m) 