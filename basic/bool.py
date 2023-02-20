# bool? True 참 / False 거짓
a = True
b = False
print(type(a))
print(type(b))

# 자료형의 참과 거짓
# "python" : 참  ## str
# "" : 거짓
# [1, 2, 3] : 참
# [] : 거짓
# (1, 2, 3) : 참
# () : 거짓
# {'a' : 1} : 참
# {} : 거짓
# 1 : 참
# 0 : 거짓
# None : 거짓

a = "안녕"
if a:
    print(a)
a = ""
if a:
    print(a)
a = [1,2,3,4]
while a:
    a.pop()
    print(a)