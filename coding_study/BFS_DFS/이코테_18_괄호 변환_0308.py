def solution(p):
    answer = ''
    # 입력이 빈 문자일 경우, 빈 문자열을 반환
    if p == '':
        return answer
    index = balanced_index(p)
    # u, v로 분리.
    u = p[:index+1]
    v = p[index+1:]
    # 문자열 u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계뿌터 다시 수행
    if check_proper(u):
        answer = u + solution(v)
    # 문자열 u가 올바른 괄호 문자열이 아니라면
    else:
        # 빈 문자열에 첫번째 문자로 (를 붙인다.
        answer = '('
        # 문자열 v에 대해 1단계뿌터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
        answer += solution(v)
        # )를 다시 붙인다.
        answer += ')'
        # u의 첫 번째와 마지막 문자를 제거하고,
        u = list(u[1:-1])
        # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        # 생성된 문자열 반환
        answer += ''.join(u)
    return answer
# 균형잡인 괄호 문자열의 인덱스 반환


def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# 올바른 괄호 문자열인지 판단


def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


# 프로그래머스에서 본 다른 풀이...b
def solution(p):
    if p == '':
        return p
    r = True
    c = 0
    for i in range(len(p)):
        if p[i] == '(':
            c -= 1
        else:
            c += 1
        if c > 0:
            r = False
        if c == 0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x: '(' if x == ')' else ')', p[1:i])))
