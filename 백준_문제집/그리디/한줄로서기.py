import sys

n=int(input())
left=list(map(int,(sys.stdin.readline().split())))
ans=[]
#뒤에서부터 끼워넣는게 포인트!!
#앞에서부터끼워넣으면 자리가 차있을때 순서가 뒤죽박죽됨.
for i in range(n):
    ans.insert(left[n-1-i],n-i)

print(*ans)