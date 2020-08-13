t=int(input())
nums=[int(input()) for _ in range(t)]

count=[1,2,4]
#끝에서부터 3개의 합을 리스트에 저장
for i in range(4,11):
    count.append(sum(count[-3:]))

for i in range(t):
    print(count[nums[i]-1])