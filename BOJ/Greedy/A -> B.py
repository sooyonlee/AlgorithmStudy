#### sol1. top-down ####
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 1

while a!=b :
    temp = b
    cnt += 1
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    if temp == b: ## 변화가 없는 경우 종료
        print(-1)
        exit(0)
else:
    print(cnt)