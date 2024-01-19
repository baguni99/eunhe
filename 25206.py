rating=['A+','A0','B+','B0','C+','C0','D+','D0','F']
grade=[4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0]

total=0 #학점 총합
result=0 #(학점*과목평점) 총합
for _ in range(20):
    s,p,g = input().split() #s:과목명, p:grade, g:rating
    p=float(p) #실수형으로 변환
    if g !='P' :   #P이면 넘어감
        total +=p
        result +=p*grade[rating.index(g)] #g값이 리스트rating에서 몇번째인지 찾고 grade에서 해당하는 학점 가져옴
print('%.6f'%(result/total)) #소수점6자리 : %.6f