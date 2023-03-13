# 한 줄 입력받아 출력하는 소스코드
import sys
# 하나의 문자열 데이터 입력받기
# rstrip() : 엔터가 줄 바꿈 기호로 입력되는데 이 공백문자 제거
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력
print(input_data)

# 1000만 개를 넘어가거나 탐색 범위의 크기가 1000억 이상이라면 이진 탐색 알고리즘 의심
# 입력 데이터가 많은 문제는 sys 라이브러리의 readline()함수 이용
