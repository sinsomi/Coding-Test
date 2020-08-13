from itertools import combinations

nums = [int(input()) for _ in range(9)]
nums.sort()
#7개씩 조합을 구해줌
for seven in combinations(nums,7):
    #그조합의 합이 100이면
    if sum(seven) == 100:
        #출력해라
        for i in seven:
            print(i)
        break