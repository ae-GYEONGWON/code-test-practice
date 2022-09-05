def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(len(citations)):
        if citations[i] == i+1:
            answer = i+1
            break
    return answer

solution([3, 0, 6, 1, 5])

# 0 5
# 1 4
# 2 3
# 3 3
# 4 2
# 5 2
# 6 1 
# # citations 이상 인용된 논문의 갯수(h)가 citations개 이상인 h의 최댓값
