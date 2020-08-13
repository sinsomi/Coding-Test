import itertools
import sys

while True:
    input_list=list(map(int,input().split()))
    if input_list[0] == 0:
        break
    k=input_list[0]
    del input_list[0]
    ans=[]

    for i in itertools.combinations(input_list,6):
        ans.append(i)

    for i in ans:
        print(*sorted(i),end='\n')
    print('')