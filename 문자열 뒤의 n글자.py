def solution(my_string, n):
    return my_string[len(my_string)-n::]
#문자열 길이에서 n을 뺀값
#::시작 인덱스부터 문자열의 끝까지 추출 -> 뒤에서부터 n개의 문자가 추출됨