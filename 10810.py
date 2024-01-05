N,M=map(int,input().split())
arr = [0]*N
for i in range(M):
    i,j,k=map(int,input().split())
    arr[i-1:j]=[k]*(j-i+1)
print(*arr)
# i번 바구니부터 j번 바구니까지에 k 번 공을 넣는다/.
# 이해안됨