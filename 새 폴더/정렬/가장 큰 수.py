def solution(numbers):
    answer = ''
    answer_list = []
    max_num = 0
    temp = ''
    a = list(map(str,numbers))
    temp_list = [list(a[i]) for i in range(len(numbers))]
    numbers.sort()
    if 1000 in numbers:
        temp = str(numbers.pop())
    while True :
        for i in range(len(temp_list)):
            if int(temp_list[i][0]) > max_num:
                max_num = int(temp_list[i][0])

        b = [temp_list[i] for i in range(len(temp_list)) if int(temp_list[i][0]) == max_num]
        b.sort(reverse = True)
    
        for i in b:
            temp_list.remove(i)
        
        if len(b) == 1:
            answer_list += b[-1]
        else:
            count1 = 0
            b2 = []
            for i in range(len(b)):
                if len(b[i]) ==1:
                    count1 += 1

            for i in range(len(b)):
                if int(b[i][1]) > max_num:
                    answer_list += b[i]
                
            answer_list += b[-1] * count

            for i in range(len(b)):
                if int(b[i][2]) <= max_num:
                    answer_list += b[i]
            
            for i in range(len(b)):
                if len(b[i]) == 2:
                    answer_list += b[i]

        max_num = 0
        count = 0
        if len(temp_list) == 0:
            break
    for i in answer_list:
        answer += i
    return answer + str(temp)

print(solution([6, 10, 2]))