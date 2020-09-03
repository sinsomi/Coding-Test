def solution(s):
    s_list=list(map(int,s.split()))
    s_list.sort()
    ans=str(s_list[0])+' '+str(s_list[-1])
    return ans
print(solution('-1 -2 -3 -4'))