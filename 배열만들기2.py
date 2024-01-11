# 1. 차집합 이용
def solution(l, r):
    answer = []
    for i in range(l,r+1) :
        answer=[]
        if not set(str(i))-set(['0','5']):
            answer.append(i)
    return answer if answer else [-1]

#2.
def solution(l, r):
    answer = []
    for i in range(l,r+1) :
        answer=[]
        if not set(str(i))-{'0','5'}:
            answer.append(i)
    return answer if answer else [-1]
#3. 중간에 answer=[] 을 없앰
def solution(l, r):
    answer = []
    for i in range(l,r+1) :
        answer=[]
        if not set(str(i))-{'0','5'}:
            answer.append(i)
    return answer if answer else [-1]