# stack = [None, None, None, None, None]
stack = [None for _ in range(5)] # list comprehension 사용
top = -1

top = top + 1
stack[top] = "커피"
top = top + 1
stack[top] = "녹차"
top = top + 1
stack[top] = "꿀물"

for i in range(len(stack)-1, -1, -1):
    print(stack[i])