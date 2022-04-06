# h,m = map(int, input().split())
# time = int(input())

# new_h = (h + (m + time) // 60) % 24

# if (m + time >= 60):
#   new_m = (m + time) % 60
#   print(new_h, new_m ,sep=' ')

# else:
#   print(new_h, m+time ,sep=' ')

h,m = map(int, input().split())
time = h * 60 + m + int(input())
print(time//60 % 24, time %60)