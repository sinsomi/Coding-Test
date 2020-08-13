def solution(arr,commands):
    ans=[]
    for start,end,k in commands:
        ans_list=arr[start-1:end]
        ans_list.sort()
        ans.append(ans_list[k-1])

    return ans
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))