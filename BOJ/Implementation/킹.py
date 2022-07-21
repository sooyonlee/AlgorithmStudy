# BOJ 1063

# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# B : 한 칸 아래로
# T : 한 칸 위로
# RT : 오른쪽 위 대각선으로
# LT : 왼쪽 위 대각선으로
# RB : 오른쪽 아래 대각선으로
# LB : 왼쪽 아래 대각선으로

king, stone, n = input().split()
k = [ord(king[0])-64, int(king[1])] # ascii 'A' = 65
s = [ord(stone[0])-64, int(stone[1])]
move = {'R': [1,0], 'L': [-1,0], 'B': [0, -1], 'T': [0,1], 'RT': [1,1], 
'LT':[-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}
move_list = [input() for _ in range(int(n))]

for m in move_list:
    nx = k[0] + move[m][0]
    ny = k[1] + move[m][1]
    if 0 < nx <= 8 and 0 < ny <= 8: # 1~8
        if nx == s[0] and ny == s[1]: # k의 이동 후 위치가 s와 같은 경우, 같이 움직여야 함
            sx = s[0] + move[m][0]
            sy = s[1] + move[m][1]
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [nx, ny]
                s = [sx ,sy]
        else:
            k = [nx, ny]
print(f'{chr(k[0]+64)}{k[1]}')
print(chr(s[0]+64)+str(s[1])) # str의 경우 '+'를 이용하면 띄어쓰기 없이 출력됨!
# print(''.join(map(str, [chr(k[0]+64), k[1]])))