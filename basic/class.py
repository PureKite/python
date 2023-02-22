result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

## but 2대의 계산기가 필요한 상황이 발생하면?
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

# 클래스 : 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀(설계도)
class Calculator: # 맨 앞글자는 대문자
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

## 클래스란? 과자 틀 => 과자(객체)
class FourCal:
    def __init__(self, first, second):  ## 예약어 / 맨 처음 실행
        self.first = first
        self.second = second
    def setdata(self, first, second):  # self : 자기 자신, 객체
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal(1, 2)
# a.setdata(1,2)
print(a.first)
print(a.second)
print(a.add())

# 클래스의 상속 : 기존의 클래스를 응용해서 사용하기 위해서
# 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용
class FourCal:
    def __init__(self, first, second):  ## 예약어 / 맨 처음 실행
        self.first = first
        self.second = second
    def setdata(self, first, second):  # self : 자기 자신, 객체
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def div(self):
        return self.first / self.second

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.add())
print(a.pow())

# 메서드 오버라이딩
class SafeFourCal(FourCal):
     def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second
        
a = SafeFourCal(4, 0)
print(a.div())  # 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(덮어쓰기)

# 클래스 변수, 객체 변수
class Family:
    lastname = "김"  # 클래스 변수
a = Family()
print(a.lastname)

Family.lastname = "박"
b = Family()
print(b.lastname)