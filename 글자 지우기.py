def solution(my_string, indices):
    answer = [i for i in my_string]
    indices.sort()
    indices.reverse()
    for j in indices:
        del answer[j]
    return "".join(answer)


def solution(my_string,indices):
    answer=''
    for i in range(len(my_string)):
        if i not in indices:
            answer+=my_string[i]
    return answer