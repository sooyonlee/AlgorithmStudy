n = int(input())
cnt = 0
temp = n

while True:
    cnt += 1
    a = temp // 10
    b = temp % 10
    c = (a+b) % 10
    temp = b*10 +c
    if n == temp :
        break

print(cnt)
    