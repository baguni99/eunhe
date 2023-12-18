def solution(my_string, overwrite_string,s) :
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer

# :s (슬라이싱)
# len 리스트의 길이를 찾는 함수