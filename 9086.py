#1.
T=int(input())
for i in range(T):
    S=input()
    print(S[0],S[-1])

# 2
T=int(input())
for i in range(T):
    S=str(input())
    print(S[0]+S[-1])
    # + : 공백없이 출력하게 함