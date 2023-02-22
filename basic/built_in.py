# abs => 절대값
print(abs(-3))
# all => 모두 참인지 검사
# any => 하나라도 참이 있는가?
# chr => ASCII 코드를 입력받아 문자 출력
# dir => 객체가 지닌 변수나 함수 보여주기
# divmod => 몫과 나머지를 튜플 형태로 돌려줌
# enumerate => 열거하다, 인덱스 값을 포함하는 객체 리턴 / 보통 for문과 함께 사용
# eval => 실행 후 결과값을 돌려줌
# filter => 함수를 통과하여 참인 것만 돌려줌
def positive(x):
    return x > 0
a = list(filter(positive, [1, -3, 2, 0, -5, 6]))
print(a)
# hex => 정수를 16진수 문자열로 변환
# id => 주소 값
# input => 사용자 입력 받는 함수
# int => 10진수 정수 형태로 변환
# isinstance => isinstance(object, class) 함수는 첫 번째 인수로 객체, 두 번째 인수로 클래스를 받는다. 입력으로 받은 객체가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 리턴한다.
# len => 길이
# list => 리스트로 변환
# map => 각 요소가 수행한 결과를 돌려줌 / lambda와 같이 많이 사용
# max => 최대 값
# min => 최소 값
# oct => 정수를 8진수로 변환
# open =>  파일 객체 리턴
# ord => 문자의 유니코드 숫자 값을 리턴하는 함수
# pow => 제곱한 결괏값을 리턴하는 함수
# range => 범위
# round => 반올림
# sorted => 정렬
# str => 문자열 반환
# sum => 입력 데이터의 합을 리턴하는 함수
# tuple => 튜플 반환
# type =>  타입 출력
# zip => 자료형을 묶어주는 역할