# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
n=int(input())
sum=0
for i in range(1,n+1) :  
    # 범위가 1부터 범위+1 까지의 형태
    sum +=i
    # sum은 i가 돌면서 1부터 n까지 더한 값
print(sum)

# 입력받은 sum +=i 는 sum=sum+i
# i=1일 때, sum=0+1
# i=2일 때, sum=1+2
# i=3일 때, sum=3+3