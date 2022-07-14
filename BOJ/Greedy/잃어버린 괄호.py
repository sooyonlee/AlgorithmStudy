# BOJ 1541
a = input().split("-")
arr = []
for i in a:
    if '+' in i:
        b = map(int, i.split("+"))
        arr.append(sum(b))
    else:
        arr.append(int(i))
print(arr[0]-sum(arr[1:]))        