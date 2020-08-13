import sys

n=int(input())
info_list=[]
for _ in range(n):
    info_list.append(list(input().split()))

info_list.sort(key=lambda x:int(x[0]))
for i in info_list:
    print(i[0],i[1])