import sys
input = sys.stdin.readline

n = int(input())
members = []

for i in range(n):
    age, name = input().split()
    members.append((int(age), name, i))
members.sort(key = lambda x: (x[0], x[2]))

for i in members:
    print(i[0], i[1])