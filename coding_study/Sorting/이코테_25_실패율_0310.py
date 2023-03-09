def solution(N, stages):
    answer = [0] * (N+2)
    # n이 전체 스테이지의 개수, stages=[]가 게임을 이용하는 사용자가 멈춰있는 스테이지 번호
    # 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
    per = []
    total = len(stages)
    for i in stages:
        answer[i] += 1
    for i in range(1, N+1):
        if total <= 0:
            per.append((0, i))
        else:
            per.append((answer[i]/total, i))
        total -= answer[i]
    per = sorted(per, key=lambda x: (-x[0], x[1]))
    answer = []
    for i in per:
        answer.append(i[1])
    # print(per)
    return answer


solution(4, [4, 4, 4, 4, 4])
