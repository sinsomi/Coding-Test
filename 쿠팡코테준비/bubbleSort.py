def bubbleSort(x):
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x

input_list=list(map(int,input().split()))

for i in bubbleSort(input_list):
    print(i,end=' ')

#2중 for문이기 때문에 시간복잡도 O(N^2)
#가장 간단하고 구현이 쉽지만 정렬속도가 느림
#인접한 2개의 원소들을 비교해서 교환해주는 과정(오른쪽끝까지 반복)
#오른쪽끝부터 가장 큰수가 정렬됨.
