import sys
input = sys.stdin.readline
ans,x,y = -1,0,0
for i in range(9):  #9*9배열 입력받기 위해 사용
    arr=list(map(int,input().split())) #한 줄을 입력받아 공백을 리스트로 변환하여 arr에 저장
    for j in range(9): #각 행의 9개 열에 대해 반복
        if arr[j]>ans: #현재위치의 값 arr[j]이 기존 최댓값 ans 보다 큰 경우에는
            ans,x,y=arr[j],i,j #ans,x,y,을 이 값으로 변경한다.
print(ans,x+1,y+1,sep="\n") #sep="\n" : 출력 간의 줄바꿈

board=[] #빈 리스트 생성
for _ in range(9):
    board.append(list(map(int,input().split()))) #9줄을 입력받아 board리스트에 각 행을 추가

x=0
y=0
max=-1

for i in range(9): #행에 대한 루프
    for j in range(9): #열에 대한 루프
        if board[i][j]>max:
            max=board[i][j]
            x=i+1
            y=j+1
print(max)
print(x,y)
