import sys

n=int(input())
matrix=[list(sys.stdin.readline().strip()) for _ in range(n)]
visited=[[0]*n]*n

dx=[0,1]
dy=[1,0]
ans=0

def check():
    ret=1
    cnt=1
    #오른쪽이랑 위쪽만 비교하면됨_왼쪽과 아래는 이미 전 좌표에서 비교한것이 됨.
    for i in range(n):
        #오른쪽 비교해서 같으면 cnt증가
        for j in range(n-1):
            if matrix[i][j]==matrix[i][j+1]:
                cnt+=1
            else:
                ret=max(ret,cnt)
                cnt=1
        ret=max(ret,cnt)
        cnt=1

        #위쪽 비교해서 같으면 cnt증가
        for j in range(n-1):
            if matrix[j][i]==matrix[j+1][i]:
                cnt+=1
            else:
                ret=max(ret,cnt)
                cnt=1
        ret = max(ret, cnt)
        cnt = 1
    return ret

#모든좌표에대해서 오른쪽과 위쪽을 탐색해줄것임
for x in range(n):
    for y in range(n):
        for k in range(2):
            nx=x+dx[k]
            ny=y+dy[k]
            if nx>=n or nx<0 or ny>=n or ny<0:
                continue
            #좌표를 swqp한 뒤에 check()함수에 넣어서 같은지 확인하고 같으면 cnt증가
            matrix[x][y],matrix[nx][ny]=matrix[nx][ny],matrix[x][y]
            ans=max(ans,check())
            #다시 좌표 원래대로 고치기
            matrix[x][y], matrix[nx][ny] = matrix[nx][ny], matrix[x][y]
print(ans)
