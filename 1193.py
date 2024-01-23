X=int(input())
line=1 #몇번째 대각선인지

while X>line : #X 가 line 보다 큰 동안 계속 반복
    X-=line #X에서 현재의 line값을 빼준다. 현재 대각선까지의 숫자를 뺀 나머지 숫자를 의미
    line +=1 #line 1 증가시키고 다음 대각선으로 이동
if line%2 ==0: #현재 대각선이 짝수라면
    a=X
    b=line-X+1
else: #홀수
    a=line-X+1
    b=X
print(a,'/',b,sep="") #sep : 출력 시 공백없이 출력