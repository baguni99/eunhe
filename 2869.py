a,b,v=map(int,input().split())
#a:달팽이가 낮에 올라갈 수 있는 높이 b:밤에 미끄러지는 높이,v : 나무 막대 길이
day=0

while 1:
    if a-b ==v:
        print(day)
        break
    a +=2
    b +=1
    day +=1
a,b,v = map(int,input().split())
day=(v-b)/(a-b)

print(int(day)if day==int(day) else int(day)+1)


a,b,v=map(int,input().split())
days=(v-b-1)//(a-b)+1 #v-b:총올라가야할 높이에서 다음날 밤에 이동한 거리를 제외하기 위해 b를 뺀다.
#최대거리 a에서 b만큼 내려간걸 빼준다. 이걸 나누면 몇일걸리는 지가 나옴
#1을 빼는 이유는 첫날 끝에서 a-b만큼 이동했기 때문
#첫 날이 시작되는 부분을 포함하기 위해 분모에 +1을 해준다.
print(days)