#선택정렬
#처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨앞에 있는 데이터와 바꿈

arr=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[min_index]>arr[j]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i] #스와프

print(arr)