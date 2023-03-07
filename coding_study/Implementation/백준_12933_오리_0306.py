duck = input()
# 오리 울음소리 순서 q -> u -> a -> c -> k
quack = 'quack'
visited = [0] * len(duck)
#
# key point! 오리가 연속으로 울기 가능 => 최소한의 오리를 찾기 위해서..!
# quack 다음 quack이 나오면 한 마리로 취급..!


def find(start):  # 오리 몇 명인지 찾는 함수
    global cnt
    j = 0
    first = 1
    for i in range(start, len(duck)):  # (duck)
        if duck[i] == quack[j] and not visited[i]:
            visited[i] = 1
            if duck[i] == 'k':
                if first:
                    cnt += 1  # 오리가 연속으로 울면 한 마리로 치기 때문에 첫 울음소리만 count
                    first = 0  # 첫 울음소리 count 했기 때문에 0으로 변경
                j = 0  # 마지막 문자인 k까지 나왔으면 다시 q부터 찾아서 비교(quack)
            else:
                j += 1  # 다음 문자 비교(quack)


if len(duck) % 5 != 0:  # quack은 5글자이기 때문에 => 5로 나누었을때 0이 아니라면 다 -1
    print(-1)
    exit()

cnt = 0
for i in range(len(duck)):  # 0부터 duck 문자열의 수까지
    if duck[i] == 'q' and not visited[i]:  # 방문하지 않은 q 탐색
        find(i)

# count의 수(오리 수)가 0이거나 visited에서 안 들린 예를 들어 qauck => 잘못된 순서일시 visited가 방문안되어있으서 -1 출력
if cnt == 0 or not all(visited):
    print(-1)
# count의 수(오리 수) 출력
else:
    print(cnt)
