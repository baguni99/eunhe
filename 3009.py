a,A=map(int,input().split())
b,B=map(int,input().split())
c,C=map(int,input().split())
d=D=0

if a==b:
    c=d
elif a==c:
    b==d
elif b==c:
    a==d
    D=a+(C-B)
if A==B:
    D=C
elif A==C:
    D=B
elif B==C:
    D=A
print(d,D)

x_nums=[]
y_nums=[]
for _ in range(3):  #x좌표, y좌표를 모은 두 개의 리스트 생성
    x,y=map(int,input().split())
    x_nums.append(x)
    y_nums.append(y)
for i in range(3): #두 개의 리스트 중에서 개수가 한 개인 요소를 찾아서 출력
    if x_nums.count(x_nums[i])==1:
        x4=x_nums[i]
    if y_nums.count(y_nums[i])==1:
        y4=y_nums[i]
print(x4,y4)