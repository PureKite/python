# def solution(s):
#     answer = 0
#     l = []
#     # 자를 수 있는 단위 찾기
#     for i in range(1, len(s)/2+1):
#         if len(s) % i == 0:
#             l.append(i)
#             l.append(len(s)//i)
#     # 문자열 압축 찾기
#     # ??
#     return answer

# 답안 예시
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위로 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]  # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):  # step별로 for문이 가능하다는 것을 까먹고 있었음..
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j+step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count)+prev if count >= 2 else prev
                prev = s[j:j+step]  # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer


s = input()
print(solution(s))
