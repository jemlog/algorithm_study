# 문제의 핵심 포인트
# - 중복되는 요소 중 하나만 가질 수 있다. -> set을 떠올려야 한다.

def solution(nums):
    answer = len(nums) / 2 if len(set(nums)) >= len(nums) / 2 else len(set(nums))
    return answer