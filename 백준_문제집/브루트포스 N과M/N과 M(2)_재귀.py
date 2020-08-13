import sys
n,m=map(int,sys.stdin.readline().split())
visited=[0]*n
ans=[]

#solve()함수먼저 실행->프린트1, 다시 for문 돌아감
#solve()함수또실행 ->프린트2, 다시 for문 돌아감
def solve(idx,depth,n,m):
    #탈출조건
    if depth==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(n):
        #idx라는 변수를 하나더줘서 idx가 i+1보다 작으면
        if(visited[i]==0 and idx<i+1):
            visited[i]=1
            #idx는 i+1로 갱신
            idx=i+1
            ans.append(i+1)
            solve(idx,depth+1,n,m)
            ans.pop()
            visited[i]=0

solve(0,0,n,m)