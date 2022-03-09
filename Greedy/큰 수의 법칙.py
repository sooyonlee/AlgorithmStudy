n, m, k = map(int, input().split())
l = list(map(int, input().split()))

max_val = max(l)
l.remove(max_val)
max_val2 = max(l)

print((max_val*(m-m%k)) + (max_val2*(m%k)))
