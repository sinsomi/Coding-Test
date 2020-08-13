import sys
n=int(input())
def ft(n):
    return n*ft(n-1) if n > 1 else 1
print(ft(n))