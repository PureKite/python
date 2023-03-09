import sys
input = sys.stdin.readline
n = int(input())
students = []
for i in range(n):
    name, s1, s2, s3 = input().split()
    students.append((name, int(s1), int(s2), int(s3)))

# 국어 점수 감소하는 순, 영어 점수 증가하는 순, 수학 점수 감소하는 순, 이름 사전순
students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])

# 백준 다른 사람의 풀이 중 시간이 빠른 풀이


def parse_line(line):
    name, kor, eng, math = line.split(' ')
    kor, eng, math = int(kor), int(eng), int(math)
    # 정렬 순서대로 return
    return -kor, eng, -math, name


data = [parse_line(input()) for _ in range(n)]
print(sorted(data))
print(*map(lambda x: x[3], sorted(data)), sep='\n')
