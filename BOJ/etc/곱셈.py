# BOJ 1629
import sys
input = sys.stdin.readline

a,b,m = map(int, input().split())

def pow(a,b,m):
    if b ==1 : 
        return a % m
    val = pow(a,b//2,m)
    val = val * val % m
    if b%2 == 0: 
        return val
    return val * a % m 

print(pow(a,b,m))