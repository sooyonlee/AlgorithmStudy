# 1541
a = input().split('-')
list = []
for i in a:
    b = i.split('+')
    sum = 0
    for j in b:
        sum += int(j)
    list.append(sum)
res = list[0]
for i in range(1, len(list)):
    res -= list[i]
print(res)
# res = list[0] - sum(list[1:])