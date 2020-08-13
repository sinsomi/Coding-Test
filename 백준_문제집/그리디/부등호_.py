n=int(input())
op=input().split()
check=[False] * 10
mx,mn='',''

def possible(i,j,k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True  #부등호가 성립하면 true

def solve_mn(cnt, s):
    global mn
    if cnt == n + 1: #숫자개수가 부등호개수보다 1개 많으면
        if not len(mn):
            mn=s
        return
    for i in range(10):
        if not check[i]:
            if cnt == 0 or possible(s[-1],str(i),op[cnt-1]):
                check[i]=True
                solve_mn(cnt+1, s+str(i)) #dfs탐색
                check[i]=False
def solve_mx(cnt, s):
    global mx
    if cnt == n + 1: #숫자개수가 부등호개수보다 1개 많으면
        if not len(mx):
            mx=s
        return
    for i in range(9,-1,-1):
        if not check[i]:
            if cnt == 0 or possible(s[-1],str(i),op[cnt-1]):
                check[i]=True
                solve_mx(cnt+1, s+str(i)) #dfs탐색
                check[i]=False
solve_mn(0,'')
solve_mx(0,'')
print(mx)
print(mn)