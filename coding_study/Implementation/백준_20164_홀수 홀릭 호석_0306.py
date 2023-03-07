n = input()
cnt = 0
min_cnt = 999
max_cnt = 0


def count_odd(arr):  # 수의 각 자리 숫자 중에서 홀수의 개수 찾기
    cnt = 0
    for i in arr:
        if int(i) % 2 == 1:
            cnt += 1
    return cnt


def dfs(n, cnt):
    global min_cnt, max_cnt
    cnt = cnt + count_odd(n)

    if len(n) == 1:  # 수가 한 자리
        min_cnt = min(min_cnt, cnt)
        max_cnt = max(max_cnt, cnt)
    elif len(n) == 2:  # 수가 두 자리
        # 각 자리의 숫자를 합쳐서 새로운 수 만들기 ex) 62 = 6 + 2 = 8
        temp = int(n) // 10 + int(n) % 10
        n = str(temp)
        dfs(n, cnt)
    else:  # 수가 3자리 이상 => 3개의 수로 분할, 3개를 더한 겂을 새로운 수로 생각
        for i in range(1, len(n)):
            for j in range(i+1, len(n)):
                temp = int(n[:i]) + int(n[i:j]) + int(n[j:])
                dfs(str(temp), cnt)


dfs(n, 0)
print(min_cnt, max_cnt)
