#선택정렬
#처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입

arr=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        #자기보다 작은 원소 만나면 멈춤
        else:
            break

print(arr)