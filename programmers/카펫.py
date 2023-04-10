def solution(brown, yellow):
    answer = []
    carpet = brown + yellow
    for i in range(int(carpet ** (1/2)), carpet+1):
        if carpet % i == 0 and i >= (carpet / i):
            answer.append([i, carpet//i])
    return check(answer, brown, yellow)


def check(answer, brown, yellow):
    for i, j in answer:
        brown_cnt = 0
        yellow_cnt = 0
        temp = [[1 for _ in range(i)] for _ in range(j)]
        for x in range(i):
            temp[0][x] = 0
            temp[j-1][x] = 0
        for y in range(j):
            temp[y][0] = 0
            temp[y][i-1] = 0
        for x in temp:
            brown_cnt += x.count(0)
            yellow_cnt += x.count(1)
        if brown == brown_cnt and yellow == yellow_cnt:
            return [i, j]


print(solution(10, 2))
