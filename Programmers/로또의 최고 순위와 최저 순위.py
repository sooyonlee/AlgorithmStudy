def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    inter= len(set(lottos) & set(win_nums))
    zero = lottos.count(0)       
    return rank[inter+zero], rank[inter]