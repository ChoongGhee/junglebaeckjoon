import math


def solution(brown, yellow):
    answer = []

    temp = int(math.sqrt(yellow))
    while temp>0:
        if yellow % temp == 0:
            quo = yellow // temp
            if (quo + 2) * (temp + 2) == brown + yellow:
                answer.append(quo + 2)
                answer.append(temp + 2)
                return answer
        temp -= 1