# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
import sys
T=int(sys.stdin.readline())
for i in range(1,T+1):
    A,B=map(int,sys.stdin.readline().split())
    print('Case #%s: %s'%(i,A+B))

# %s : 문자열
#  문자열 포맷팅을 이용해 i과 A+B를 문자열로 변환한 후 