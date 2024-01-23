number=int(input()) #색종이의 수
canvas=[[0]*101 for i in range(101)] #101*101배열의 이차원 배열 만들기
for _ in range(number): #색종이 수만큼 반복
    left,bottom=map(int,input().split())

    for i in range(10): #10*10크기의 색종이를 도화지에 붙이는 부분
        for j in range(10):
            canvas[left+i][bottom+j]=1 #색종이가 도화지에 붙는 부분을 1로 표시
black_paper=0
for i in canvas:
    black_paper+=sum(i)
print(black_paper)