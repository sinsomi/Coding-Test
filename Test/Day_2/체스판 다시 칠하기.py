#1.8x8크기로 자를수있는경우의수
#2.각각의 경우마다 WB를 바꿔주는경우의수
import sys

n,m=map(int,input().split())
matrix=[]
for _ in range(n):
    matrix.append(list(sys.stdin.readline().strip()))
ans=2500
for i in range(n-7):
    for j in range(m-7):

        # WB
        cnt = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if matrix[k][l]=='W' and (k+l)%2!=0:
                    cnt+=1
                elif matrix[k][l]=='B' and (k+l)%2==0:
                    cnt+=1
        ans=min(cnt,ans)

        # BW
        cnt = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if matrix[k][l] == 'B' and (k + l) % 2 != 0:
                    cnt += 1
                elif matrix[k][l] == 'W' and (k + l) % 2 == 0:
                    cnt += 1
        ans = min(cnt, ans)
print(ans)