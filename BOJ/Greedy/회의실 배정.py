n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
table.sort(key = lambda x:(x[1], x[0]))

cnt = 0
last = 0

for start, end in table:
    if start >= last:
        cnt += 1
        last = end
print(cnt)        