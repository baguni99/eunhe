a,b=map(int,input().split())

while 0<a and b<10:
    # 0<a,b<10인 경우에만 반복할 것이다
    if a!=0 and b!=0:
        # 0 두 개가 입력되면 반복문 끝. 0 두 개가 아니면 반복
        print(a+b)
    a,b = map(int,input().split())

while True:
    (a,b)=map(int,input().split())
    if a==0 and b==0:
        break
    print(a+b)