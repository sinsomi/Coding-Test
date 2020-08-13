t=int(input())

def solve():
    n=int(input())
    nums=input().split()
    ans=[]
    real_ans=[]

    for i in nums:
        ans.append([nums.count(i),i])
    for i in nums:
        ans.sort(reverse=True)
    return print('#'+str(n)+' '+str(ans[0][1]))

for i in range(t):
    solve()