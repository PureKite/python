n = int(input())
number = [input() for _ in range(n)]
number2 = []
for i in number:
    s = 0
    for j in range(len(i)):
        if i[j].isnumeric():
            s += int(i[j])
    number2.append((i, s))

number = sorted(number2, key=lambda x: (len(x[0]), x[1], x))

for i in number:
    print(i[0])

# 간단한 풀이
print(*sorted([*open(0)][1:], key=lambda x: (len(x), sum(int(i)
      for i in x if '/' < i < ':'), x)), sep="")
