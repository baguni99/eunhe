
word = input()
l = len(word)
li = []
for i in range(l):
    li.append(word[i:])
li = sorted(li)
for i in range(l):
    print(li[i])