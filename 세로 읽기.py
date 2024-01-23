def solution(my_string, m, c):
    answer = '' #결과 문자열
    temp_list = [] #일정 간격으로 나눠진 부분 문자열을 저장할 리스트
    for i in range(len(my_string)//m): #문자열을 일정간격m으로 나누어 temp_list에 저장
        temp_list.append(list(my_string[i*m:i*m+m])) #i번째 부분 문자열을 추출하여 리스트로 변환
        
    for i in temp_list:
        answer += i[c-1] #temp_list에 저장된 각 부분 문자열에서 c-1 위치의 문자를 추출하여 answer에 추가
    return answer