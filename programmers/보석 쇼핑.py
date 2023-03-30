# def solution(gems):
#     answer = []
#     name = {}
#     for i in gems:
#         name[i] = 0
#     n = len(name)-1
#     while n < len(gems):
#         answer.append((0, n))
#         n += 1
#     for i, j in answer:
#         while i < len(gems)-1 and j < len(gems)-1:
#             i += 1
#             j += 1
#             answer.append((i, j))
#     answer = list(set(answer))
#     answer = sorted(answer, key=lambda x: (abs(x[0]-x[1]), x[0], x[1]))

#     for i, j in answer:
#         for k in gems[i:j+1]:
#             name[k] += 1
#         if 0 not in name.values():
#             return i+1, j+1
#         for i in name.keys():
#             name[i] = 0

def solution(gems):
    answer = [0, len(gems)]
    size = len(set(gems))

    start = 0
    end = 0
    gem_dict = {gems[0]: 1}

    while start < len(gems) and end < len(gems):
        if len(gem_dict) == size:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            else:
                gem_dict[gems[start]] -= 1
                if gem_dict[gems[start]] == 0:
                    del gem_dict[gems[start]]
                start += 1
        else:
            end += 1

            if end == len(gems):
                break
            gem_dict[gems[end]] = gem_dict.get(gems[end], 0) + 1
    return [answer[0]+1, answer[1]+1]


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
