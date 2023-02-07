def is_stack_full():
    global SIZE, stack, top     # 전역변수 참조
    if top >= SIZE-1:
        return True
    # else:
    return False


def is_stack_empty():
    global SIZE, stack, top  # 전역변수 참조
    if top == - 1:
        return True
    # else:
    return False


def push(data):
    global SIZE, stack, top  # 전역변수 참조
    if is_stack_full():
        print("Stack is Full")
        return
    top = top + 1
    stack[top] = data

def pop():
    global SIZE, stack, top  # 전역변수 참조
    if is_stack_empty():
        print("Stack is empty")
        return
    temp = stack[top]
    stack[top] = None
    top = top - 1
    return temp

def peek():
    global SIZE, stack, top  # 전역변수 참조
    if is_stack_empty():
        print("Stack is empty")
        return None
    return stack[top]


SIZE = 5
stack = [None for _ in range(SIZE)]     #list comprehension
top = -1


if __name__ == "__main__":
    while True:
        menu = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나를 선택 ")
        if menu == 'X' or menu == 'x':
            break
        elif menu == 'I' or menu == "i":
            data = input("입력할 데이터: ")
            push(data)
            print("스택 상태: ", stack)
        elif menu =="e":
            data = pop()
            print("추출한 데이터: ", data)
            print("스택 상태: ", stack)
        elif menu == 'v':
            data = peek()
            print("확인한 데이터: ", data)
            print("스택 상태: ", stack)
        else:`
            print("다시 입력")

    print("프로그램 종료")