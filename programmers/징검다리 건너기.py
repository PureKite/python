# 정확성은 다 맞았지만.. 효율성 0점...
# def solution(stones, k):
#     answer = 0
#     while True:
#         count = 0
#         for i in range(len(stones)):
#             if stones[i] != 0:
#                 stones[i] -= 1
#         answer += 1
#         for i in range(len(stones)):
#             if count >= k:
#                 break
#             if stones[i] == 0:
#                 count += 1
#             else:
#                 count = 0
#         if count >= k:
#             break
#     return answer


# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

# 다른 사람 코드 참고 : https://wiselog.tistory.com/65
# 이진 탐색을 사용했어야 했다!!!!
# 스스로 최적화 방법 생각해내기


def solution(stones, k):
    left = 1
    right = max(stones) + 1  # 최댓값으로 right하면 더 빠를 것 같음
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                right = mid - 1
                break
        else:
            left = mid + 1

    return left


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
