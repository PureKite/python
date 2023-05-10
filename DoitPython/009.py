# 계속 시간초과로 인해 답 찾아봄..ㅜㅜ..
import sys

input = sys.stdin.readline

checkList = [0] * 4
myList = [0] * 4
checkSecret = 0


def myadd(c):  # 새로 들어온 문자를 처리하는 함수
    global checkList, myList, checkSecret
    if c == "A":
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == "C":
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == "G":
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    if c == "T":
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1


def myremove(c):
    global checkList, myList, checkSecret
    if c == "A":
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == "C":
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == "G":
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    if c == "T":
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1


s, p = map(int, input().split())
dna = str(input().rstrip())
checkList = list(map(int, input().split()))
count = 0

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(p):
    myadd(dna[i])

if checkSecret == 4:
    count += 1

for i in range(p, s):
    j = i - p
    myadd(dna[i])
    myremove(dna[j])
    if checkSecret == 4:
        count += 1

print(count)
