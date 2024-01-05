# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
N= int(input())
N_list=list(map(int,input().split()))
v=int(input())
print(N_list.count(v))

# 1. N : 넣어야 할 정수의 갯수
# 2. N_list : n개의 값을 입력받아 리스트 형태로 구성
# 3. v : 찾을 정수
# 4. count(v)를 통해 리스트에 v가 몇 개 있는 지 출력
