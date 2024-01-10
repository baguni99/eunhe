def solution(numLog):
    result=[]
    prev_num = numLog[0]

    for i in range(1,len(numLog)):
        diff = numLog[i] - prev_num   #numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과. 현재값과 이전 값 간의 차이 

        if diff == 1:
            result.append("w")
        elif diff == -1:
            result.append("s")
        elif diff == 10:
            result.append("d")
        elif diff == -10:
            result.append("a")

        prev_num=numLog[i] #현재값을 이전값으로 설정하여 다음 순회에서 사용
    return ''.join(result) #리스트에 저장된 문자열을 결합하여 반환