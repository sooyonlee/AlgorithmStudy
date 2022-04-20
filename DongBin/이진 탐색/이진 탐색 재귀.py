def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우
    elif array[mid] > target:
        binary_search(array, target, start, mid-1)
    else:
        binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1) # 인덱스는 0부터 시작하므로 n-1 
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
