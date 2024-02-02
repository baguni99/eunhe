def solution(arr):
    if 2 not in arr:
        return[-1]
    start_index=arr.index(2)   #2으 ㅣ인덱스 검색
    end_index=arr[::-1].index(2)  #2의 인덱스 역순 검색
    end_index=len(arr)-1-end_index
    return arr[start_index:end_index+1]