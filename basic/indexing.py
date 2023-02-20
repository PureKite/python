a = "hi123"

print(a[0])
print(a[1])
print(a[-1])


# 슬라이싱
print(a[2:4])
print(a[:5:2]) #[이상:미만:간격]


# 문자열 포매팅(Formatting)
b = "I eat %d apples." % 3
print(b)
number = 10
day = "three"
c = "I ate %d apples. so I was sick for %s days." % (number, day)
print(c)

# 문자열 포맷 코드
# %s : 문자열  => 숫자도 가능
# %c : 문자 1개
# %d : 정수
# %f : 부동소수
# %o : 8진수
# %x : 16진수
## %% : Literal % (문자 % 자체)

d = "I eat {0} apples".format(3)
print(d)
e = "%0.4f" % 3.14151617
print(e)