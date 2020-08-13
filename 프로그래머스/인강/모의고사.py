def solution(answers):
    cnt1,cnt2,cnt3=0,0,0
    person1=[1,2,3,4,5]
    person2=[2,1,2,3,2,4,2,5]
    person3=[3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if person1[i%5]==answers[i]:
            cnt1+=1
        if person2[i%8]==answers[i]:
            cnt2+=1
        if person3[i%10]==answers[i]:
            cnt3+=1
    pre_ans=[cnt1,cnt2,cnt3]
    ans=[]
    for i in range(len(pre_ans)):
        if pre_ans[i]==max(pre_ans):
            ans.append(i+1)
    return print(ans)
solution([1,3,2,4,2])