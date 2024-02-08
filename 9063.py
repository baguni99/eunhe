import sys
input=sys.stdin.readline

x,y=[],[]
for i in range(int(input())):
    a,b=map(int,input().split())
    x.append(a);y.append(b)
print((max(x)-min(x))*(max(y)-min(y)))

#입력의 모든 꼭짓점을 포함하는 가장 작은 직사각형의 넓이를 구하면 된다.
# 모든 꼭짓점의 x,y 좌표를 기록한 뒤 각각 가장 큰 것에서 가장 작은 것을 뺀 것을 곱하면 된다.