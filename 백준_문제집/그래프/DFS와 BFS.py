N, M, V = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1

#DFS
def dfs(current_node, row, foot_prints):
    #DFS를 수행하는 결과를 저장하는 리스트; 시작정점을 우선 넣어둠
    foot_prints += [current_node]
    #matrix를 탐색해 나감
    for search_node in range(len(row[current_node])):
        #만약 matrix[current_node][search_node]가 이어져있고
        #search_node가 방문하지 않은곳이라면
        #그곳을 더깊이 탐색해나감; 시작정점을 search_node로 재귀호출
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints

#BFS
def bfs(start):
    #queue에 시작정점을 저장해둠
    queue = [start]
    #BFS를 수행하는 결과를 저장하는 리스트; 시작정점을 우선 넣어둠
    foot_prints = [start]
    #queue가 빌때까지 반복
    while queue:
        #queue의 값을 빼서 시작정점으로 대입
        current_node = queue.pop(0)
        #matrix를 탐색해 나감
        for search_node in range(len(matrix[current_node])):
            #만약 matrix[current_node][search_node]가 이어져있고
            #search_node가 방문하지 않은것이라면
            #foot_prints에 search_node를 담고
            #queue에도 search_node를 담음 -> 그럼 다음번에 탐색할 정점이 search_node가 됨
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints


print(*dfs(V, matrix, []))
print(*bfs(V))