def solution(s):
    answer = ''
    nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for idx, num in enumerate(nums):
        if num in s:
            s = s.replace(num, str(idx))
    answer = int(s)

    return answer