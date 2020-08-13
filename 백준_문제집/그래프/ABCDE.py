import sys

#(AB,BC,CD,DE)친구관계가 성립하는 5명이 있으면 1, 없으면 0을 출력
def dfs(v,k):
    global state
    #방문했다고 1로 표시
    visited[v]=1
    #종료조건은 총 사람이 5명이 되면 종료
    if k==5:
        state=1
        return
    #v정점과 연결된 정점들에 대해 탐색
    else:
        for e in adj[v]:
            if not visited[e]:  #방문하지 않은 정점에 대해서
                dfs(e,k+1)      #재귀호출(depth는 1씩더해가면서)
                visited[e]=0    #다음 정점탐색을 위해 다시 0으로 바꿔주기

n,m=map(int,input().split())
visited=[0]*n
adj=[[] for _ in range(n+1)]
state=0

#친구관계를 입력받아서 adj리스트에 각 연결된 점을 저장해주는 코드
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

#main함수 부분
for v in range(n):
    dfs(v,1)
    visited[v]=0
    if state:
        break
print(state)