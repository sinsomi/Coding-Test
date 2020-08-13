num_list = []
ans = []
count = 1
possibility = True
for i in range(int(input())):
    num = int(input())
    while count <= num:             # count와 num이 같은수를 찾는다.
        num_list.append(count)      # 그전까진 1부터 count까지 num_list에 저장한다.
        ans.append('+')      # 저장과 동시에 push라는 말이므로 +를 추가해준다
        count += 1
    if num_list[-1] == num:
        num_list.pop()              # num과 num_list의 마지막 값이 같다면 pop해준다.
        ans.append('-')      # pop를 했으니 -를 추가한다.
    else:
        possibility = False         # num과 num_list의 마지막 값이 다르다면 수열이 성립하지않는다.

if possibility == False:
    print('NO')
else:
    for j in ans:
        print(j)