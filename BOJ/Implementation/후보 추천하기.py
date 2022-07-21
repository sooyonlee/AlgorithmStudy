# BOJ 1713
n = int(input())
m = int(input())
student = list(map(int, input().split()))
dict = {}

for s in student:
    if s not in dict:
        # 비어있는 틀이 없는 경우 추천수가 가장 적은 학생 삭제
        # 여러명이면 그 중 먼저 들어온 원소 삭제
        if len(dict) == n:
            min_value = min(dict.values())
            min_list = []
            for key, val in dict.items():
                if min_value >= val:
                    min_list.append(key)
            dict.pop(min_list[0]) # 먼저 들어온 원소 삭제
        dict[s] = 1
    else:
        dict[s] += 1

print(*sorted(dict.keys()))