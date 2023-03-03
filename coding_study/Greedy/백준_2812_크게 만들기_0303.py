n, k = map(int, input().split())
nums = input().rstrip()
stack = []

for num in nums:
    while stack and stack[-1] < num and k > 0:
        stack.pop()
        k -= 1
    stack.append(num)

if k > 0:
    print(''.join(stack[:-k]))
    ## 여기 반례 찾음 7 3 7654321
else:
    print(''.join(stack))