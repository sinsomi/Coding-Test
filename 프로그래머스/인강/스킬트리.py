def solution(skill,skill_trees):
    result=0
    skill=list(skill)
    for skill_tree in skill_trees:
        tmp=[]
        ans = 0
        for val in skill_tree:
            #skill에 없는 문자는 무시
            if val not in skill:
                continue
            else:
                tmp.append(val)
                print(tmp)
        for i in range(len(tmp)):
            print(tmp[i],skill[i])
            if tmp[i]==skill[i]:
                ans+=1
        if len(tmp)==ans:
            result+=1
    return result
print(solution('cbd',['bacde','cbadf','aecb','bda']))