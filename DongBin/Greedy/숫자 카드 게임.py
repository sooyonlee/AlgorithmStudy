n,m = map(int, input().split())

min_list =[]
for i in range(n):
  rows = list(map(int, input().split()))
  min_list.append(min(rows))

print(max(min_list))

###########################
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)