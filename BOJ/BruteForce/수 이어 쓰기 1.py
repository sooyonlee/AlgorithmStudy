n = int(input())
ans = 0
start = 1
length = 1
while start <= n:
    end = 10 * start - 1
    if end > n:
        end = n
    ans += (end-start+1)*length
    start *= 10
    length += 1
print(ans)