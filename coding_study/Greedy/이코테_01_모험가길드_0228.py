n = input()
data = list(map(int, input().split()))

data.sort()
## 정렬을 사용하면 된다고 생각은 나는데 그 후에 어떻게 구현을 해야할지 모르겠음

## 해설을 보고 난 후 구현(코드는 안 본 상태)
result = 0
group = set(data)
for i in group:
    if i <= data.count(i):
        result += 1
print(result)



## 답안 예시
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# result = 0 # 총 그룹의 수
# count = 0 # 현재 그룹에 포함된 모험가의 수

# for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
#     count += 1 # 현재 그룹에 해당 모험가를 포함시키기
#     if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
#         result += 1 # 총 그룹의 수 증가시키기
#         count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
# print(result)