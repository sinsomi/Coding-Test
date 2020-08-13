"""solution함수는 x,y,d1,d2값과 맵의 전체 크기의 한변인 n과 선거구 인원인 p가 주어졌을 때,
   선거구의 인원수의 최대값과 최솟값의 차를 반환하는 함수입니다."""
def solution(x,y,d1,d2,n,p):
	#area는 각 선거구의 인원수를 받는다.
    area=[0 for _ in range(5)]
    #map1은 각 구역을 선거구역으로 나누기 위해 만든 맵
    map1=[[0 for _ in range(n)] for _ in range(n)]
    # 먼저 경계선을 구역5로 할당한다.
    for i in range(d1+1):
        map1[x+i][y-i]=5
        map1[x+d2+i][y+d2-i]=5
    for i in range(d2+1):
        map1[x+i][y+i]=5
        map1[x+d1+i][y-d1+i]=5
    for i in range(d1):
        k=1
        while(map1[x+i+k][y-i]!=5):
            map1[x+i+k][y-i]=5
            k+=1
    #경계선 내부구역을 구역 5로 지정
    for i in range(d2):
        k=1
        while(map1[x+i+k][y+i]!=5):
            map1[x+i+k][y+i]=5
            k+=1
    #경계선 외부 구역을 구역1~4로 각각 나눈다.
    for i in range(n):
        for j in range(n):
        	#구역1
            if i<x+d1 and j<=y and map1[i][j]==0:
                map1[i][j]=1
            #구역2
            elif i<=x+d2 and j>y and map1[i][j]==0:
                map1[i][j]=2
            #구역3
            elif x+d1<=i and j<y-d1+d2 and map1[i][j]==0:
                map1[i][j]=3
            #구역4
            elif i>x+d2 and j>=y-d1+d2 and map1[i][j]==0:
                map1[i][j]=4
    #이제 map1의 값에 따라 area값을 추가해준다.
    for i in range(n):
        for j in range(n):
            area[map1[i][j]-1]+=p[i][j]
    # 구역의 최댓값과 최솟값의 차이를 반환한다.
    return (max(area)-min(area))
# 구역 크기인 n을 받는다.
n=int(input())
# 최종값인 answer를 -1로 선언
answer=-1
# 각 셀마다 인구수를 population에 입력 받는다.
population=[]
for _ in range(n):
    population.append(list(map(int,input().split())))
# x의 범위는 위에서 2칸 이상이어야 한다.
for i in range(n-2):
	# y의 범위는 양 사이드에서 1칸씩 안에 있어야한다.
    for j in range(1,n-1):
        for k in range(1,j+1):
            for s in range(1,n-1-i-k):
                try:
                    sub=solution(i,j,k,s,n,population)
                    #만약 처음으로 solution함수를 돌린 것이라면 sub값을 answer로 할당
                    if answer==-1:
                        answer=sub
                    # 만약 answer값이 sub값보다 클 경우 sub값으로 answer값을 변경
                    elif answer>sub:
                        answer=sub
                except:
                    continue
print(answer)