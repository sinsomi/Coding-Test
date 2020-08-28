from collections import deque

def bfs(i,j,drum):
    queue=deque()
    stop=0
    queue.append([i,j])

    while queue:
        r,c=queue.popleft()

        if r==len(drum)-1:
            if drum[r][c]=='#':
                return True
            elif drum[r][c]=='*' and stop<2:
                return True
            #이건 없어야할 코드,,
            #else:
                #return False

        if drum[r][c]=='#':
            if r+1<len(drum):
                queue.append([r+1,c])

        elif drum[r][c]=='>':
            if c+1<len(drum[0]):
                queue.append([r,c+1])

        elif drum[r][c]=='<':
            if c-1>=0:
                queue.append([r,c-1])

        elif drum[r][c]=='*':
            if stop<1:
                if r + 1 < len(drum):
                    queue.append([r+1,c])
                    stop+=1
            else:
                break

    return False

def solution(drum):
    cnt=0
    for i in range(len(drum)):
        if bfs(0,i,drum) is True:
            cnt+=1
    return cnt

print(solution(['######','>#*###','####*#','#<#>>#','>#*#*<','######']))