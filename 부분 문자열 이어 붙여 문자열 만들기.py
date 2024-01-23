def solution(my_strings, parts):
    answer = ''
    for i , indices in enumerate(parts): #parts의 각 요소를 순회하면서 인덱스 i와 해당하는 부분 문자열의 시작과 끝 인덱스를 나타내는 indices를 얻는다.
        start,end = indices #각 부분 문자열의 시작과 끝 인덱스를 변수에 할당
        current_string = my_strings[i] #현재 순회 중인 'my_strings'의 원소를 가져온다.

        reconstructed_string=current_string[:start]+current_string[start:end+1]+current_string[end+1:] #이어붙여서 문자열 완성
        answer+=reconstructed_string #이어붙인 문자열을 answer에 추가
    return answer