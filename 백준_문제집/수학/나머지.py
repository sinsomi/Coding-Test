import sys
A,B,C=map(int,sys.stdin.readline().split()) #띄어쓰기 간격으로 입력받아옴
print((A+B)%C,(A%C+B%C)%C,(A*B)%C,((A%C)*(B%C))%C,sep='\n') #sep을 이용해서 여러줄로 출력