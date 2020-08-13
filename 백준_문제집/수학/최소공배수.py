import sys

#최대공약수 함수
def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
#최소공배수 함수
def lcm(x,y):
    return(x*y//gcd(x,y))

n=int(input())
answer=[]
for i in range(n):
    #두수를 n번만큼 받아오기
    x,y=map(int,sys.stdin.readline().split())
    #answer리스트에 구해준 최소공배수 저장
    answer.append(lcm(x,y))
#answer리스트 모두 출력
for i in answer:
    print(i)