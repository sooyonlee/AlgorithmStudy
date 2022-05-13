import heapq
import sys
input = sys.stdin.readline

n = int(input())
cards = []
ans = 0

for _ in range(n):
    heapq.heappush(cards, int(input()))

while len(cards) > 1:
    plus = heapq.heappop(cards) + heapq.heappop(cards)
    ans += plus
    heapq.heappush(cards, plus)

print(ans)
