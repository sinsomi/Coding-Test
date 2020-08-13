import sys

n=int(input())
words=[sys.stdin.readline().strip() for _ in range(n)]
str_nums=[]
int_nums=[]

for word in words:
    t=1
    for ch in word[::-1]:
        str_nums.append(str(t)+ch)
        t=int(t)*10
str_nums.sort()

for i in range(len(str_nums)):
    for j in range(i+1,len(str_nums)-1):
        if str_nums[i][-1]==str_nums[j][-1]:
            str_nums.remove(str_nums[j])

w=9
for i in range(len(str_nums)):
    int_nums.append(str_nums[i][:-1])
    int_nums[i]=int(int_nums[i])*w
    w-=1

s=0
for k in int_nums:
    s+=k
print(s)
