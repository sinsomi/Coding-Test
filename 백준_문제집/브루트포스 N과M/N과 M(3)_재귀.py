import sys
n,m=map(int,sys.stdin.readline().split())
ans=[]

#solve()함수먼저 실행->프린트1, 다시 for문 돌아감
#solve()함수또실행 ->프린트2, 다시 for문 돌아감
def solve(depth,n,m):
    #탈출조건
    if depth==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(n):
        ans.append(i+1)
        solve(depth+1,n,m)
        ans.pop()

solve(0,n,m)