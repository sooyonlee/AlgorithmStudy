import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

c_temp = cost[0]
ans = 0
for d,c in zip(dist, cost): 
    if c_temp > c:
        c_temp = c
    ans += d * c_temp

print(ans)