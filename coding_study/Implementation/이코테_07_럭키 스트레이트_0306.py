# 정수 입력
n = input()
# 정수 길이 반으로 나누기
num = len(n) // 2
# 왼쪽 부분 오른쪽 부분 합하기
left = 0
right = 0
for i in range(len(n)):
    if num <= i:
        right += int(n[i])
    else:
        left += int(n[i])
if left == right:
    print('LUCKY')
else:
    print('READY')
