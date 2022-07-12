# BOJ 11047번
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
types = [int(input()) for i in range(n)]
types.sort(reverse=True)

cnt = 0
for i in types:
    if k//i > 0:
        cnt += k//i
        k -= i*(k//i)
print(cnt)