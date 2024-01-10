N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1  #i와 j를 0-based index로 변환.
    arr[i:j+1] = arr[i:j+1][::-1] #리스트 슬라이싱 : arr[i:j+1]범위에 해당하는 부분을 역순으로 뒤집고, 원래 리스트에 할당
print(*arr)
