n,m = map(int, input().split())
arr = [list(map(int, input())) for i in range(n)]

result = []
for k in range(min(n,m)):
    for i in range(n-k):
        for j in range(m-k):
            if arr[i][j] == arr[i+k][j] == arr[i][j+k] == arr[i+k][j+k]:
                result.append((i+1)**2)
print(max(result))

# cnt = 1
# for i in range(n):
#     for j in range(m):
#         if j<m and arr[i][j] in arr[i][j+1:]:
#           for k in range(m-1,j,-1):
#             if arr[i][j] == arr[i][k]:
#               len = k-j
#               if i+len < n and arr[i+len][j] == arr[i][j] and arr[i+len][k] == arr[i][j]:
#                 cnt = max(cnt, (len+1)**2)
# print(cnt)

