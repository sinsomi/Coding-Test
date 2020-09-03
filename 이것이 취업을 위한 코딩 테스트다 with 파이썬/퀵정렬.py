#퀵정렬
arr=[7,5,9,0,3,1,6,2,4,8]

def quick_sort(arr):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr)<=1:
        return arr

    pivot=arr[0] #피벗은 첫번째원소
    tail=arr[1:] #피벗을 제외한 원소

    left=[x for x in tail if x<=pivot] #분할된 왼쪽부분
    right=[x for x in tail if x>pivot] #분할된 오른쪽부분
    print(left,'pivot',pivot,right)

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체리스트 반환
    return quick_sort(left)+[pivot]+quick_sort(right)


print(quick_sort(arr))
