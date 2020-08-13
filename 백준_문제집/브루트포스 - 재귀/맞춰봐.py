#입력으로 주어지는 합의 부호에 맞는 숫자 배열을 출력하는 문제다.
#총 21개의 숫자 중에서 N개의 숫자를 골라야 한다.
#일반적인 재귀 함수를 통해 브루트 포스로 구현하면 시간 초과가 나기 쉬우므로, 백트래킹 기법을 사용해야 한다.
#숫자의 범위 (-10 ~ 10) 만큼 재귀 함수를 호출한다.
#하나의 숫자를 고를 때마다, 이 숫자가 주어진 부호에 맞는지 확인한다.
#해당 숫자가 가능하다면, 다음 재귀 함수를 호출한다.
#하나의 숫자 리스트만 찾으면 되므로, 찾으면 바로 프로그램을 종료한다.

n=int(input())
a=[[0]*n for _ in range(n)]
oper=list(input())
v,k=[],0

def possible(idx):
    s=0
    for i in range(idx,-1,-1):
        s+=v[i]
        if a[i][idx] == '+' and s<=0:
            return False
        if a[i][idx] == '0' and s!=0:
            return False
        if a[i][idx] == '-' and s>=0:
            return False
    return True

def solve(idx):
    if idx==n:                #재귀탈출
        print(' '.join(map(str,v)))
        exit(0)              #답이 여러가지일 경우 하나만 출력해야 하므로 탈출
    for i in range(-10,11):  #숫자의 범위 (-10 ~ 10)만큼 재귀호출
        v.append(i)
        if possible(idx):
            solve(idx+1)
        v.pop()

for i in range(n):
    for j in range(i,n):
        a[i][j]=oper[k]
        k+=1
solve(0)