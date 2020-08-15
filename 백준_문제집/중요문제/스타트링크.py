from collections import deque
f,s,g,u,d=map(int,input().split())

visit=[0]*1000001
queue=deque()
def bfs(v):
    queue.append(v)
    visit[v]=1
    while queue:
        v=queue.popleft()

        if v==g:
            return visit[v]-1

        for nv in (v+u,v-d):
            if (1<=nv<1000001) and visit[nv]==0:
                visit[nv]=visit[v]+1
                #print(nv)
                queue.append(nv)
    return 'use the stairs'
print(bfs(s))