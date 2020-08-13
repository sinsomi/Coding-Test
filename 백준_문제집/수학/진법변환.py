import sys
input_str,input_int=sys.stdin.readline().split()
input_int=int(input_int)
ans=0
#nums 딕셔너리에 각각 저장
nums={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,
      'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,
      'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}
#input_str인 ZZZZZ의 역순으로 -1 간격으로(맨끝 Z부터 젤처음 Z까지)
#i는 4부터 0까지, v는 Z부터Z까지
for i,v in enumerate(input_str[::-1]):
    #ans는 진법변환한 수를 더해두는것
    #nums[v]는 KEY가 v(=Z)인 VALUE를 출력 => 35
    ans+=(nums[v])*(input_int**i)
print(ans)