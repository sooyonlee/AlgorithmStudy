def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        compress = ''
        prev = s[:step]
        cnt = 1
        for i in range(step, len(s), step):
            if step == s[i:i+step]:
                cnt += 1
            else:
                compress += str(cnt) + prev if cnt >=2 else prev
                prev = s[i:i+step]
                cnt = 1
        compress += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(compress))
    return answer