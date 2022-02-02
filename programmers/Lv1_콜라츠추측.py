def solution(num):
    # 재귀 예상 
    cnt = 0 
    answer = repeat(cnt, num)
    return answer

def repeat(cnt, num):
    if num == 1 :
        return cnt 
    if num%2 == 0 :
        num = num/2
    elif num%2 != 0 :
        num = 3*num + 1
    cnt = cnt + 1 
    return repeat(cnt, num)

print(solution(6))
