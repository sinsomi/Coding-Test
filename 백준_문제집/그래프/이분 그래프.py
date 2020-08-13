#이분그래프: 인접한 노드는 서로 다른색의 노드로 구분되고, 그래프 내의 모든 노드를 두가지 색으로만 칠할 수 있는 그래프
import sys
sys.setrecursionlimit(100000)

#DFS로 탐색
def dfs(current,group,a,visited):
    visited[current]=group
    for i in a[current]:
        #방문하지 않은 노드를 탐색
        if visited[i]==0:
            # 2개의 그룹으로 나눈다고 가정하고 1과 -1의 그룹으로 구분
            if dfs(i,-group,a,visited) is False:
                return False
        #만약 다음노드가 이미방문한 노드라면, 현재노드의 그룹번호와 다음 노드의 번호가 같은지 확인
        elif visited[i]==visited[current]:
            #번호가 같으면 인접한 노드이므로 false를 리턴
            return False
    #DFS탐색 끝날때까지 False를 리턴하지 않으면 모든노드를 이분화하는 것에 성공한것이므로 true
    return True

for _ in range(int(sys.stdin.readline())):
    v,e=map(int,sys.stdin.readline().split())
    a=[[] for _ in range(v+1)]
    visited=[0]*(v+1)
    for _ in range(e):
        x,y=map(int,sys.stdin.readline().split())
        a[x].append(y)
        a[y].append(x)
    ans=True
    for i in range(1,v+1):
        if visited[i]==0:
            if dfs(i,1,a,visited) is False:
                ans=False
                break
    print('YES' if ans else 'NO')