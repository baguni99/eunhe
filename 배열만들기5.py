def solution(intStrs, k, s, l):
    return [int(i[s:s+l]) for i in intStrs if int(i[s:s+l])>k]

#반복문을 이용해 intStrs의 [s:s+l] 부분을 슬라이싱한 값이 k보다 크면 배열에 추가
