# BOJ 16935
# 짲응나 아주~~^_^
def calc_1():
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        temp[i] = arr[n-1-i]
    return temp

def calc_2():
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[i][m-1-j]
    return temp
  
def calc_3():
    temp = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            temp[j][n-1-i] = arr[i][j]
    return temp  
  
def calc_4():
    temp = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            temp[m-1-j][i] = arr[i][j]
    return temp

def calc_5():
    temp = [[0] * m for _ in range(n)]
    # 1->2
    for i in range(n//2):
        for j in range(m//2):
            temp[i][j+m//2] = arr[i][j]
    # 2->3            
    for i in range(n//2):
        for j in range(m//2, m):
            temp[i+n//2][j] = arr[i][j]
    # 3->4       
    for i in range(n//2, n):
        for j in range(m//2,m):
            temp[i][j-m//2] = arr[i][j]
    # 4->1
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i-n//2][j] = arr[i][j]
    return temp

def calc_6():
    temp = [[0]*m for _ in range(n)]
    # 1->4
    for i in range(n//2):
        for j in range(m//2):
            temp[i+n//2][j] = arr[i][j]
    # 4->3
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i][j+m//2] = arr[i][j]
    # 3->2
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp[i-n//2][j] = arr[i][j]
    # 2->1
    for i in range(n//2):
        for j in range(m//2, m):
            temp[i][j-m//2] = arr[i][j]
    return temp
    
import sys
input = sys.stdin.readline
n,m,r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
todoList = list(map(int, input().split()))

for todo in todoList:
    if todo == 1:
        arr = calc_1()
    elif todo == 2:
        arr = calc_2()
    elif todo == 3:
        arr = calc_3()
        n,m = m,n # 90도 뒤집으면 배열 크기가 바뀜
    elif todo == 4:
        arr = calc_4()
        n,m = m,n # 얘도 마찬가지
    elif todo == 5:
        arr = calc_5()
    else:
        arr = calc_6()

for i in arr:
    print(*i) # unpack