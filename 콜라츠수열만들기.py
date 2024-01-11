x=int(input())
for i in range(x):
    if x%2==0 :
        x/2
    else : 3*x+1

def solution(x):
    answer=[x]
    while x != 1:
        if x %2 ==0 :
            x//=2
        else:
            x=3*x+1
        answer.append(x)
    return answer
