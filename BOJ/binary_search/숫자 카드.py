import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            print(1, end=' ')
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    else: 
        print(0, end=' ')
    
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

for i in b:
    binary_search(a, i, 0, len(a)-1)