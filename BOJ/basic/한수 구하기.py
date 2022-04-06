def HanNum(N):
    cnt = 0
    for i in range(1, N+1):
        b = list(map(int, str(i)))
        if i < 100 :
            cnt +=1
        elif b[2] - b[1] == b[1] - b[0]:
            cnt +=1
    return cnt
N = int(input())
print(HanNum(N))