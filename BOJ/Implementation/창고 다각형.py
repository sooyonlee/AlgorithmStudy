n = int(input())
pillar = []
maxL = 0
maxH = 0
for _ in range(n):
    L,H = map(int, input().split())
    pillar.append([L,H])
    if maxL < L:
        maxL = L
    if maxH < H:
        maxH = H
        maxIndex = L

pillarList = [0]*(maxL+1)
for l,h in pillar:
    pillarList[l] = h

total = 0
temp = 0
# 왼쪽 ~ 가장 높은 기둥까지
for i in range(maxIndex+1):
    if pillarList[i] > temp:
        temp = pillarList[i]
    total += temp

# 오른쪽 ~ 가장 높은 기둥
temp = 0
for i in range(maxL, maxIndex, -1):
    if pillarList[i] > temp:
        temp = pillarList[i]
    total += temp

print(total)

