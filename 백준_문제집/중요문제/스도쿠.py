import sys

maps=[list(map(int,[p for p in sys.stdin.readline().split()])) for _ in range(9)]

#정사각형말고 한줄로 이해했을때 푼 코드
for val_list in maps:
    nums=[0]*9
    zero=[]
    val=[]
    cnt=0
    for i in val_list:
        if i==0:
            zero.append(cnt)
        else:
            nums[i-1]=True
        cnt+=1
    for i in range(len(nums)):
        if nums[i]==0:
            val.append(i+1)
    for i in range(len(val)):
        val_list[zero[i]]=val[i]

for i in maps:
    print(*i)