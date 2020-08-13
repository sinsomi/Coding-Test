import sys

def bigger(a,b):
    if a>b: return a
    return b

def can_read():
    cnt=0
    #입력받은 단어들을 검사
    for i in range(len(strs)):
        read=True
        string = strs[i]
        #입력받은 단어의 알파벳이 a,n,t,i,c중 하나가아니면 False
        for j in range(len(string)):
            if alpha[ord(string[j])-ord('a')] is False:
                read=False
                break
        # 입력받은 단어의 알파벳이 a,n,t,i,c중 하나라면 True
        # cnt증가
        if read is True:
            cnt+=1

    return cnt

def dfs(idx,cnt):
    global ans
    if cnt==k:
        ans=bigger(ans,can_read())
        return

    #알파벳 26개를 검사
    for i in range(26):
        #이미 읽을 수 있다고 한 알파벳은 넘어감
        if alpha[i] is True:
            continue

        #알파벳을 True로 하고 cnt를 증가시켜 재귀호출
        alpha[i]=True
        dfs(i,cnt+1)
        #다시 False로
        alpha[i]=False

n,k=map(int,input().split())
strs=[sys.stdin.readline().strip() for _ in range(n)]
ans=0
alpha=[False for _ in range(26)]
alpha[ord('a')-ord('a')]=True
alpha[ord('c')-ord('a')]=True
alpha[ord('i')-ord('a')]=True
alpha[ord('n')-ord('a')]=True
alpha[ord('t')-ord('a')]=True
if k<5:
    exit(0)
k=k-5
dfs(0,0)
print(ans)
