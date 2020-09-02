def solution(begin, target, words):
    visit = [0]*len(words)
    res = []
    def dfs(word,depth):
        #return 된후 어떻게 동작하는지?
        if word==target:
            res.append(depth)
            return
        else:
            for i in range(len(words)):
                # 이미 비교한 단어는 비교하지 않음
                if visit[i]==1:
                    continue
                
                #begin단어랑 비교될단어랑 글자차이수=cnt
                cnt=0
                for j in range(len(word)):
                    if word[j]!=words[i][j]:
                        cnt+=1
                
                #글자가 하나만 다르면 dfs탐색
                if cnt==1:
                    visit[i]=1
                    print(words[i],depth+1)
                    dfs(words[i],depth+1)
                    visit[i]=0
    dfs(begin,0)
    if len(res)==0:
        return 0
    return min(res)
print(solution('hit','cog',['hot','dot','dog','lot','log','cog']))