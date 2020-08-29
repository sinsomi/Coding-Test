def solution(n, computers):
    answer = 0
    queue = []
    visited = [0]*n

    while 0 in visited:
        queue.append(visited.index(0))
        print(queue)
        while queue:
            node = queue.pop(0)
            visited[node] = 1
            print(visited)
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    queue.append(i)
        answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))