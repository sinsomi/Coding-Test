#VER1
#1.각블록을구해주기
#2.각높이에 블록을 모양마다 채우기
#3.블록을 채운 후에, 각 칸마다 위에서부터 1이 채워져있는지 확인
#4.위에서 1이채워져있는데 밑으로 내려가다가 0인 부분이 나오면 안되는 경우.
#5.밑으로 내려가다가 0인부분이 없으면 되는 경우.

#VER2
#1. 각블록마다 회전하여 놓았을때 딱맞을 수 있는 높이의 경우를 구해줌
#2. 그 경우에 해당하면 ans를 1씩 증가시킴

import sys

c,p=map(int,input().split())
fd=list(map(int,sys.stdin.readline().split()))

ans=0
if p==1:
    #ㅣ모양의 블럭은 모든열에 놓을 수 있기 때문에 c만큼 경우의 수를 더함
    ans=ans+c  #0
    for i in range(c-3):
        #0000
        if fd[i] == fd[i + 1] and fd[i + 1] == fd[i + 2] and fd[i + 2] == fd[i + 3]:
            ans+=1
if p==2:
    for i in range(c-1):
        #00
        if fd[i] == fd[i + 1]:
            ans+=1
if p==3:
    for i in range(c-2):
        #001
        if fd[i] == fd[i + 1] and fd[i + 1] == fd[i + 2] - 1:
            ans+=1
    for i in range(c-1):
        #10
        if fd[i] == fd[i + 1] + 1:
            ans+=1
if p==4:
    for i in range(c-2):
        #100
        if fd[i] == fd[i + 1] + 1 and fd[i + 1] == fd[i + 2]:
            ans+=1
    for i in range(c-1):
        #01
        if fd[i] == fd[i + 1] - 1:
            ans+=1
if p==5:
    for i in range(c-2):
        #000
        if fd[i] == fd[i + 1] and fd[i + 1] == fd[i + 2]:
            ans+=1
        #101
        if fd[i] == fd[i + 1] + 1 and fd[i + 1] == fd[i + 2] - 1:
            ans+=1
    for i in range(c-1):
        #10
        if fd[i] == fd[i + 1] - 1:
            ans+=1
        #10
        if fd[i] == fd[i + 1] + 1:
            ans+=1
if p==6:
    for i in range(c-2):
        #000
        if fd[i]==fd[i+1] and fd[i+1]==fd[i+2]:
            ans+=1
        #011
        if fd[i]==fd[i+1]-1 and fd[i+1]==fd[i+2]:
            ans+=1
    for i in range(c-1):
        #00
        if fd[i]==fd[i+1]:
            ans+=1
        #20
        if fd[i]==fd[i+1]+2:
            ans+=1
if p==7:
    for i in range(c-2):
        #000
        if fd[i]==fd[i+1] and fd[i+1]==fd[i+2]:
            ans+=1
        #110
        if fd[i]==fd[i+1] and fd[i+1]==fd[i+2] + 1:
            ans+=1
    for i in range(c-1):
        #02
        if fd[i]==fd[i+1]-2:
            ans+=1
        #00
        if fd[i]==fd[i+1]:
            ans+=1

print(ans)
