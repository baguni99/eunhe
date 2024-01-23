n=int(input())
num=1 #첫번째 숫자
cnt=6 #등차수열
room=1 #지나가는 방의 수

if n==1 :
    print(1)
else:
    while True:
        num=num+cnt
        room+=1
        if n<=num:
            print(room)
            break
        cnt+=6

n= int(input()) #벌집의 숫자
nums_pileup=1 #벌집의 갯수
cnt=1 
while n>nums_pileup :
    nums_pileup +=6*cnt #벌집이 6의 배수로 증가
    cnt+=1
print(cnt)
