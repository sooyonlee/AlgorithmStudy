from itertools import permutations
n = int(input())
k = int(input())
nums = [input() for _ in range(n)]

nPr = permutations(nums, k)

ans = []
for i in nPr:
    ans.append("".join(i))
    
print(len(set(ans)))