S=input()
A=list(range(97,123))
answer=[]
for i in A:
    answer.append(S.find(chr(i)))
print(*answer)
#2
S=input()
A="abcdefghijklmnopqrstuvwxyz"
for i in A:
    print(S.find(i),end=' ')