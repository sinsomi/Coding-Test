import math
import itertools


def isPrime(n):
    sqrtn=int(math.sqrt(n))
    for i in range(2,sqrtn+1):
        if n%i==0:
            return False
    return True

def solution(nums):
    ans=0
    for i in itertools.combinations(nums,3):
        sum_list = 0
        for j in i:
            sum_list+=j
        if isPrime(sum_list) is True:
            ans+=1
    return ans
print(solution([1,2,3,4]))
