n = int(input())

data = []
for _ in range(n):
    input_data = input().split()
    data.append((input_data[0], input_data[1]))

data = sorted(data, key=lambda student: student[1])

for student in data:
    print(student[0], end=' ')
