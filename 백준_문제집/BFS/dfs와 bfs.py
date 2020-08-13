#세팅
n,m,v=map(int,input().split())
matrix=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    link=list(map(int,input().split()))
    matrix[link[0]][link[1]]=1
    matrix[link[1]][link[0]]=1

def dfs(current_node,matrix,foot_prints):
    foot_prints+=[current_node]
    #현재노드와 연결된 노드가 있는지 탐색
    for search_node in range(n+1):
        if matrix[current_node][search_node] and search_node not in foot_prints:
            #연결된노드로 재귀호출하였을 때 리턴된 foot_prints값을 갱신
            foot_prints=dfs(search_node,matrix,foot_prints)
    return foot_prints

def bfs(start):
    queue=[start]
    foot_prints=[start]
    while queue:
        current_node=queue.pop(0)
        for search_node in range(n+1):
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints+=[search_node]
                queue+=[search_node]
    return foot_prints
print(*dfs(v,matrix,[]))
print(*bfs(v))
