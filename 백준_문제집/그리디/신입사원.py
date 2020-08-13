import sys

t=int(input())

for _ in range(t):
    n=int(input())
    rank=sorted([list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)],
                key=lambda x:x[0])
    cnt=1 #서류등수1등은 나머지들보다 무조건 우수하므로 1은 +해주고 들어감
    min=rank[0][1]

    for i in range(1,n):
        if rank[i][1]<min:
            cnt+=1
            min=rank[i][1] #여태지나온 지원자들의 면접등수를 각각비교하면 시간초과
                           #그러므로 변수 min을 사용하여 여태 지나왔던 지원자들의 면접등수
                           #중에서 가장 좋은 면접등수를 저장한다.
                           #특정지원자 i의 면접등수와 min만 비교하여도 파악가능
    