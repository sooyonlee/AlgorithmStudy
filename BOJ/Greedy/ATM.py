n = int(input())
p = list(map(int, input().split()))
p.sort()

res = 0
accum = 0
for i in p:
    accum += i 
    res += accum
print(res)