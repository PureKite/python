# 파일 생성하기
# f = open("새파일.txt", 'w') #  파일 객체 = open(파일 이름, 파일 열기 모드)
# f.close()

# 파일 열기 모드
# r : 읽기 모드 - 파일을 읽기만 할 때 사용
# w : 쓰기 모드 - 파일에 내용을 쓸 때 사용
# a : 추가 모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

# 파일을 쓰기 모드로 열어 내용 쓰기
f = open("새파일.txt", 'w', encoding='UTF-8')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 파일 읽기
f = open("새파일.txt", 'r', encoding='UTF-8')
line = f.readline()
print(line)
f.close()

f = open("새파일.txt", 'r', encoding='UTF-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# readlines 함수 사용하기
f = open("새파일.txt", 'r', encoding='UTF-8')
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()

# read 함수
f = open("새파일.txt", 'r', encoding='UTF-8')
data = f.read()
print(data)
f.close()

# 파일에 새로운 내용 추가하기
f = open("새파일.txt",'a', encoding='UTF-8')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with문과 함께 사용하기 == close 자동
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")