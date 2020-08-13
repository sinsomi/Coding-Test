import sys
n,m=map(int,sys.stdin.readline().split())
visited=[0]*n
ans=[]

#만약 m=2, nums=[1,7,8,9]이면
#1번solve()함수 실행 -> 2번solve() 실행
#2번solve() -> 3번solve() 실행
#3번solve()는 depth==2이므로 출력하고 종료
#2번solve()로 돌아가서 pop()하고 for문 실행
#또 3번solve()만나서 출력하고 종료
#즉 1번solve()는 젤처음 1을제어, 2번solve()는 1뒤에 1,7,8,9를 제어
#3번solve()는 2번slove()에서 (1,1)(1,7)(1,8)(1,9)를 하나씩 실행시킬때마다 출력하고 리턴됨.
def solve(depth,n,m):
    #탈출조건
    if depth == m:
        print(' '.join(map(str,ans)))
        return
    for i in range(len(visited)):
        #탐색 안했다면
        if not visited[i]:
            visited[i]=1
            ans.append(i+1)
            #재귀호출
            solve(depth+1,n,m)
            visited[i]=0
            ans.pop()

solve(0,n,m)