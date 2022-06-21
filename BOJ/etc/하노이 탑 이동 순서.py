# BOJ 11729번
def hanoi(start, end, n):
    if n == 1:
        print(start, end)
        return 
    hanoi(start, 6-start-end, n-1) # step 1 (start에 있는 n-1개의 탑을 가운데로 옮기기)
    print(start, end) # step 2 (맨 밑에 있는 탑 3번으로 옮기기)
    hanoi(6-start-end, end, n-1) # step 3 (가운데 있는 탑을 3번으로 옮기기)

n = int(input())
print(2**n-1)
hanoi(1,3,n)