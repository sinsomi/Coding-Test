import sys
def mergeSort(x):
    if len(x)<=1:
        return x

    left=mergeSort(x[:len(x)//2])
    right=mergeSort(x[len(x)//2:])

    #오른쪽 왼쪽 반토막씩 내는 과정
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            x[k]=left[i]
            i+=1
        else:
            x[k]=right[j]
            j+=1
        k+=1

    #병합하는 과정
    if i==len(left):
        while j<len(right):
            x[k]=right[j]
            j+=1
            k+=1
    elif j==len(right):
        while i<len(left):
            x[k]=left[i]
            i+=1
            k+=1
    return x

nums=[int(sys.stdin.readline()) for i in range(int(sys.stdin.readline().strip()))]

for value in mergeSort(nums):
    print(value)