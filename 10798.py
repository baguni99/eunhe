words=[]
length=[]
for i in range(5):
    word=input()
    words.append(word)
    length.append(len(word))
rst=''
for i in range(max(length)): #가장 긴 단어의 길이를 기준으로 
    for j in range(5): #세로로 나열된 결과
        if i < length[j]: #현재 단어의 길이보다 i가 작으면 
            rst+=words[j][i] #세로로 글자를 가져옴
print(rst)
