def solution(progresses, speeds):
    answer = []
    while progreesses :
        progresses += speeds
        num = 0
        while progresses[0] >= 100:
            del progresses[0]
            num += 1
    return answer