def solution(num_list):
    answer=0
    x=1
    sum=0

    for i in num_list:
        x*=i
        sum +=i
    if x<sum**2:
        answer=1
    else :
        answer=0
    return answer