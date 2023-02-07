def is_queue_full():
    global size, queue, front, rear
    if rear == SIZE -1:
        return True
    else:
        return False

def is_queue_empty():
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def enqueue(data):
    global size, queue, front, rear
    if is_queue_full():
        print("Queue is full!")
        return
    rear = rear + 1
    queue[rear] = data


def dequeue():
    global size, queue, front, rear
    if is_queue_empty():
        print("Queue is empty!")
        return
    front = front + 1
    data = queue[front]
    queue[front] = N


# 전역 변수
size = 5
front = rear = -1
queue = [None for _ in range(size)]

