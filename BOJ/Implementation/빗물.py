# BOJ 14719번
H, W = map(int, input().split())
W_list = list(map(int, input().split()))

maxH = 0
for idx, h in enumerate(W_list):
    if maxH < h:
        maxH = H
        maxIndex = idx

total = 0
temp = 0
for i in range(maxIndex+1):
    if W_list[i] > temp:
        temp = W_list[i]
    total += temp

temp = 0
for i in range(W-1, maxIndex, -1):
    if W_list[i] < temp:
        temp = W_list[i]
    total += temp

print(total-sum(W_list))