def solution(arr):
    arr_sum=0
    str_arr=str(arr)
    for i in range(len(str_arr)):
        arr_sum+=int(str_arr[i])
    if arr%arr_sum!=0:
        return False
    return True

print(solution(11))
