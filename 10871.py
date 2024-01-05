# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
N,X=map(int,input().split())
A=list(map(int,input().split()))
for i in range(N):
    if A[i] < X :
        print (A[i],end=" ")

# if문을 이용해서 A에 있는 숫자들이 X 보다 작을 때 출력하기
        # end=" "를 이용해서 공백 생성