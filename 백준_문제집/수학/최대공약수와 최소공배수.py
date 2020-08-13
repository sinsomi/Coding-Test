import sys

def gcd(x,y):
    #y가 0이 될때까지 반복
    while(y):
        #y를 x에 대입, x%y를 y에 대입
        x,y=y,x%y
    return x
def lcm(x,y):
    #x,y의 곱에서 x,y의 최대공약수를 나눠주면 최소공배수
    return (x*y//gcd(x,y))

def solve():
    x, y = map(int, sys.stdin.readline().split())
    temp = 0
    print(gcd(x,y),lcm(x,y),sep='\n')
solve()