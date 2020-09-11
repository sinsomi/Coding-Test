def solution(brown, yellow):
    ans = []
    width=brown+yellow
    for i in range(width+1,1,-1):
        if width%i==0:
            x=i
            if x in ans:
                break
            y=width//i
            ans+=[x,y]
    print(ans)
    return ans[-2:]
print(solution(50,22))