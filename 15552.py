# 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

# C++을 사용하고 있고 cin/cout을 사용하고자 한다면, cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고, endl 대신 개행문자(\n)를 쓰자. 단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등 C의 입출력 방식을 사용하면 안 된다.

# Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다. BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.

# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

T=int(input())

for i in range(T):
    A,B=map(int,input().split())
    print (A+B)
# input은 사용자로부터 입력을 받은 후에 입력받은 표현식을 분류함 -> 입력받기 전까지 프로그램 흐름 중지 
import sys
T=int(sys.stdin.readline())
for i in range(T) :
    A,B=map(int,sys.stdin.readline().split())
    print (A+B)

# sys.stdin : 파일 객체. 뒤에 read(), readline()을 붙여서 한 줄씩 혹은 한 번에 다 릭게 할 수 있음
    # input과 달리 입력 프롬포트 미노출