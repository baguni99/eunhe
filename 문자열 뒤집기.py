def solution(my_string, s, e):
    answer = list(my_string) #문자열을 리스트로 변환
    tmp=list(my_string) #부분 문자열을 뒤집기 위한 리스트
    tmp=tmp[s:e+1] #주어진 범위의 부분 문자열 추출
    tmp=tmp[::-1] # 그 부분 문자열을 뒤집음
    answer[s:e+1]=tmp #뒤집은 부분 문자열을 원래 문자열에 적용
    answer=''.join(answer) #리스트를 다시 문자열로 변환
    return answer