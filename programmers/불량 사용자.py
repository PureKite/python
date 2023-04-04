# def solution(user_id, banned_id):
#     answer = [[] for _ in range(len(banned_id))]
#     banned = []
#     user = []

#     for i in range(len(banned_id)):
#         banned.append(list(banned_id[i]))
#     for i in range(len(user_id)):
#         user.append(list(user_id[i]))

#     for i in range(len(banned)):
#         flag = False
#         for j in user:
#             if len(banned[i]) != len(j):
#                 continue
#             for k in range(len(banned[i])):
#                 if banned[i][k] == j[k]:
#                     flag = True
#                 elif banned[i][k] == '*':
#                     flag = True
#                 else:
#                     flag = False
#             if flag == True:
#                 answer[i].append(''.join(j))
#     return answer

from itertools import permutations


def check(user, banned):
    for i in range(len(banned)):
        if len(banned[i]) != len(user[i]):
            return False
        for j in range(len(banned[i])):
            if banned[i][j] == '*':
                continue
            if banned[i][j] != user[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    for user in permutations(user_id, len(banned_id)):
        if check(user, banned_id):
            if set(user) not in answer:
                answer.append(set(user))

    print(answer)
    return len(answer)


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
# 순열
# print(list(permutations(["frodo", "fradi", "crodo", "abc123", "frodoc"], 2)))
# 조합
# print(list(combinations(["frodo", "fradi", "crodo", "abc123", "frodoc"], 2)))
